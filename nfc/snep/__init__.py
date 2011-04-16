# -----------------------------------------------------------------------------
# Copyright 2009,2010 Stephen Tiedemann <stephen.tiedemann@googlemail.com>
#
# Licensed under the EUPL, Version 1.1 or - as soon they 
# will be approved by the European Commission - subsequent
# versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the
# Licence.
# You may obtain a copy of the Licence at:
#
# http://ec.europa.eu/idabc/eupl
#
# Unless required by applicable law or agreed to in
# writing, software distributed under the Licence is
# distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied.
# See the Licence for the specific language governing
# permissions and limitations under the Licence.
# -----------------------------------------------------------------------------
#
# Implementation of the Simple NDEF Exchange Protocol (SNEP)
# 

from nfc.snep.server import SnepServer
from nfc.snep.client import SnepClient
from nfc.snep.client import SnepError

Success = 0x81
NotFound = 0xC0
ExcessData = 0xC1
BadRequest = 0xC2
NotImplemented = 0xE0
UnsupportedVersion = 0xE1
