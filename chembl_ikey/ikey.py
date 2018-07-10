__author__ = 'mnowotka'

import hashlib
from chembl_ikey import ikey_base26
from ikey_base26 import base26_triplet_1
from ikey_base26 import base26_triplet_2
from ikey_base26 import base26_triplet_3
from ikey_base26 import base26_triplet_4
from ikey_base26 import base26_dublet_for_bits_56_to_64
from ikey_base26 import base26_dublet_for_bits_28_to_36

#-----------------------------------------------------------------------------------------------------------------------

INCHI_STRING_PREFIX = "InChI="
LEN_INCHI_STRING_PREFIX = len(INCHI_STRING_PREFIX)

#-----------------------------------------------------------------------------------------------------------------------

def get_sha256(text):
    hash = hashlib.sha256()
    hash.update(text)
    return hash.digest()

#-----------------------------------------------------------------------------------------------------------------------

def inchiToInchiKey(szINCHISource):

    flagstd = 'S'
    flagnonstd = 'N'
    flagver = 'A'
    flagproto = 'N'
    pplus = "OPQRSTUVWXYZ"
    pminus = "MLKJIHGFEDCB"

    if not szINCHISource:
        return None
    slen = len(szINCHISource)

    if slen < LEN_INCHI_STRING_PREFIX + 3:
        return None

    if not szINCHISource.startswith(INCHI_STRING_PREFIX):
        return None

    if szINCHISource[LEN_INCHI_STRING_PREFIX] != '1':
        return None

    bStdFormat = None
    pos_slash1 = LEN_INCHI_STRING_PREFIX + 1

    if szINCHISource[pos_slash1] == 'S':
        bStdFormat = 1
        pos_slash1 += 1

    if szINCHISource[pos_slash1] != '/':
        return None

    if not szINCHISource[pos_slash1+1].isalnum() and szINCHISource[pos_slash1+1] != '/':
        return None

    string = szINCHISource[LEN_INCHI_STRING_PREFIX:].strip()

    if not string:
        return None

    aux = string[(pos_slash1 - LEN_INCHI_STRING_PREFIX) + 1:]
    slen = len(aux)
    proto = False
    end = 0

    for idx, ch in enumerate(aux):
        if ch == '/':
            cn = aux[idx+1]
            if cn == 'c' or cn == 'h' or cn == 'q':
                continue
            if cn == 'p':
                proto = idx
                continue
            if cn == 'f' or cn == 'r':
                return None
            end = idx
            break

    if end == (slen - 1):
        end += 1

    if not proto:
        smajor = aux[:end]
    else:
        smajor = aux[:proto]

    if proto:
        nprotons = int(aux[proto + 2:end])
        if nprotons > 0:
            if nprotons > 12:
                flagproto = 'A'
            else:
                flagproto = pplus[nprotons-1]

        elif nprotons < 0:
            if nprotons < -12:
                flagproto = 'A'
            else:
                flagproto = pminus[-nprotons-1]
        else:
            return None

    sminor = ''
    if end != slen:
        sminor = aux[end:]
    if len(sminor) < 255:
        sminor += sminor

    flag = flagstd if bStdFormat else flagnonstd

    digest_major = get_sha256(smajor)
    digest_minor = get_sha256(sminor)
    major = base26_triplet_1(digest_major) + base26_triplet_2(digest_major) + base26_triplet_3(digest_major) + \
                                base26_triplet_4(digest_major) + base26_dublet_for_bits_56_to_64(digest_major)
    minor = base26_triplet_1(digest_minor) + base26_triplet_2(digest_minor) + \
                                base26_dublet_for_bits_28_to_36(digest_minor)
    return "%s-%s%s%s-%s" % (major, minor, flag, flagver, flagproto)


#-----------------------------------------------------------------------------------------------------------------------


