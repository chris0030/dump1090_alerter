import csv

MODEL = {
    "A319": "Airbus A-319",
    "B788": "BOEING 787-8 Dreamliner",
    "A320": "Airbus A320-214",
    "A333": "Airbus A330-343X",
    "GL7T": "Bombardier BD700-Global",
    "B748": "Boeing 747-8F",
    'C295': 'CASA C-295 MPA',
    'RQ4': 'Northrop Grumman MQ-4C Triton',
    'BE20': 'Hawker Beechcraft Corp King Air 200GT',
    'AC90': 'Commander 690D Jetprop 900 ',
    'AS32': 'Eurocopter Super Puma AS.332 C1e',
    'H25B': 'Hawker Beechcraft Corp Hawker 900XP',
    'FA50': 'Dassault Falcon 50',
    'EC45': 'Eurocopter UH-72A Lakota',
    'A139': 'AgustaWestland AW-139',
    'F900': 'Dassault Falcon 900EX EASy',
    'B737': 'Boeing C-40C Clipper',
    'BE9L': 'Beech T-44A Pegasus',
    'C130': 'Lockheed C-130R Hercules',
    'A342': 'Airbus A340 212',
    'GLF4': 'Gulfstream IV',
    'FA20': 'Dassault HU-25C+ Guardian',
    'GLF3': 'Gulfstream C-20A',
    'B190': 'Beech 1900 D',
    'DH8C': 'De Havilland Canada DHC-8 CC-142',
    'AN72': 'Antonov An-72',
    'C680': 'Cessna Citation Sovereign',
    'FA7X': 'Dassault Falcon 7X',
    'FA8X': 'Dassault Falcon 8X',
    'IL76': 'Ilyushin IL-78 MKI',
    'CL30': 'Bombardier Challenger 300',
    'GLF2': 'Gulfstream G1159B',
    'C560': 'Cessna Citation V',
    'B350': 'Beech King Air B350',
    'CN35': 'CASA HC-144A Ocean Sentry',
    'C27J': 'Alenia C-27J Spartan',
    'C56X': 'Cessna Citation XLS',
    'GLF5': 'Gulfstream Aerospace C-37B',
    'TEX2': 'Beechcraft T-6C+ Texan II',
    'B738': 'Boeing P-8A Poseidon',
    'CL2T': 'Bombardier CL-415 T',
    'CP23': 'CAP Aviation CAP-232',
    'H47': 'Boeing-Vertol CH-147F Chinook',
    'B744': 'Boeing 747 412F',
    'RJ1H': 'Avro 146 RJ100',
    'B748': 'Boeing 747-8ZV BBJ',
    'GLF6': 'Gulfstream Aerospace G650 ER',
    'EH10': 'EH Industries EH.101 Merlin Mk.643',
    'C30J': 'Lockheed CC-130J-30 Hercules',
    'GLEX': 'Bombardier E-11A',
    'PC12': 'Pilatus U-28A Spectre',
    'PC24': 'Pilatus PC-24',
    'E145': 'Embraer ERJ-145 VC-99A',
    'F70': 'Fokker 70',
    'C208': 'Cessna 208 B',
    'D228': 'HAL/Dornier Do 228 201',
    'HA4T': 'Hawker Beechcraft Corp Hawker 4000',
    'CL60': 'Canadair Challenger 601',
    'A320': 'Airbus A320 232SL',
    'A332': 'Airbus A330 243',
    'C17': 'Boeing CC-177 Globemaster III',
    'TB30': 'Aerospatiale Epsilon TB.30',
    'A343': 'Airbus A340 313X',
    'J328': 'Dornier Do 328 Jet 310',
    'MD87': 'McDonnell Douglas DC-9 87',
    'F28': 'Fokker F28 1000C',
    'DH8D': 'De Havilland Canada DHC-8 402 NG',
    'IL62': 'Ilyushin IL-62 M',
    'A345': 'Airbus A340 541',
    'LYNX': 'Westland Lynx Mk.21B',
    'AT76': 'Avions de Transport Regional ATR 72 600',
    'P68': 'VulcanAir P.68 Observer 2',
    'B722': 'Boeing 727 230',
    'E170': 'Embraer EMB-170 SL',
    'B762': 'Boeing KC-46A Pegasus',
    'E35L': 'Embraer Legacy 600',
    'C25A': 'Cessna 525A CitationJet CJ2',
    'LJ60': 'Bombardier Learjet 60',
    'AT43': '1991 AEROSPATIALE/AERITALIA ATR 42-320',
    'BE30': 'Beech King Air 300',
    'E110': 'Embraer EMB-110 C-95BM',
    'ARVA': 'Israel Aircraft Industries Arava 201',
    'DC3T': 'Douglas DC-3 BT-67',
    'B752': 'Boeing 757 23A',
    'B733': 'Boeing 737 330QC',
    'B732': 'Boeing 737 2X9',
    'C25B': 'Cessna 525B Citationjet CJ-3',
    'LJ40': 'Bombardier Learjet 40 XR',
    'DH8B': 'Bombardier DHC-8 202',
    'B788': 'Boeing 787-8',
    'C501': 'Cessna Citation I',
    'G150': 'Gulfstream Aerospace G150',
    'EC25': 'Eurocopter EC725 H-36',
    'B429': 'Bell 429 Global Ranger',
    'AN12': 'Shaanxi Y-8',
    'A319': 'Airbus ACJ319 VC-1A',
    'F16': 'General Dynamics F-16C Fighting Falcon',
    'A140': 'Antonov An-140 100',
    'A148': 'Antonov An-148 100B',
    'T134': 'Tupolev Tu-134 B-3',
    'T204': 'Tupolev Tu-214 PU-SBUS',
    'L410': 'Let L-410 UVP-E3',
    'IL18': 'Ilyushin IL-20 M',
    'A124': 'Antonov An-124',
    'T154': 'Tupolev Tu-154 M',
    'BER2': 'Beriev Ber-200 ChS',
    'AN30': 'Antonov An-30',
    'IL96': 'Ilyushin IL-96 VVIP',
    'LJ31': 'Bombardier Learjet 31 A',
    'M326': 'Aermacchi MB.326 E',
    'NH90': 'NH Industries NH90 TTH',
    'P180': 'Piaggio P-180 Avanti II',
    'AT44': 'Avions de Transport Regional ATR 42 400MP',
    'AT45': 'Avions de Transport Regional ATR 42 500',
    'A169': 'LEONARDO AW.169 UH-169B',
    'M346': 'Aermacchi T.346A',
    'P06T': 'Tecnam P.2006T',
    'A149': 'AgustaWestland AW149',
    'TOR': 'Panavia Tornado IDS',
    'A109': 'AgustaWestland A.109 E',
    'P66T': 'Piaggio P.166 DP-1-VMA',
    'M339': 'Aermacchi MB.339 CM',
    'B412': 'Bell 412 EP',
    'AMX': 'Aeritalia AMX ACOL',
    'G222': 'Aeritalia-Fiat G.222 MC-27J',
    'B703': 'Boeing KC-137E 320C',
    'C650': 'Cessna Citation VII',
    'A400': 'Airbus Military A400M',
    'EC35': 'Eurocopter EC135 P2+',
    'AJET': 'Dassault-Breguet Dornier Alpha Jet',
    'P3': 'Lockheed P-3C Orion',
    'A310': 'Airbus CC-150 304/MRTT',
    'AAT3': 'Aero AT-3 R100',
    'WACF': 'Waco UPF-7',
    'A359': 'Airbus A350-941',
    'D140': 'S.A.N. Jodel D.140R Abeille',
    'G120': 'Grob G-120 TP-A',
    'CE43': 'CERVA CE.43 Guepard',
    'AS65': 'Helibrás HM-1 Panther',
    'SR22': 'Cirrus Design SR22',
    'SR20': 'Cirrus Design SR20 T-53A',
    'GAZL': 'Aerospatiale Gazelle SA.342 M',
    'TIGR': 'Eurocopter Tiger EC665 UHT',
    'PUMA': 'IAR Puma IAR.330 M',
    'AS55': 'Eurocopter Twin Squirrel AS.355 N',
    'PC6T': 'Pilatus PC-6/B2-H4 Turbo Porter',
    'TBM7': 'SOCATA TBM 700',
    'AS50': 'Eurocopter AS.350 B2',
    'PC21': 'Pilatus PC-21',
    'E121': 'Embraer 121 Xingu AN',
    'DHC6': 'Viking Air DHC-6 Twin Otter 400',
    'F2TH': 'Dassault Falcon 2000EX',
    'E300': 'Extra EA.330 SC',
    'C160': 'VFW Transall C-160D',
    'C135': 'Boeing WC-135C',
    'K35R': 'KC-135R',
    'E3CF': 'Boeing E-3C Sentry',
    'CKUO': 'AIDC F-CK-1 Ching-kuo A',
    'F406': 'Reims-Cessna F406 Caravan II',
    'S2P': 'Grumman Firecat',
    'FA50?': 'Hawker Beechcraft Corp King Air B350',
    'C206': 'Cessna TU206G Turbo Stationair 6',
    'F100': 'Fokker F100',
    'RFAL': 'Dassault Rafale B',
    'RAFL': 'Dassault Rafale B',
    'MIR2': 'Dassault Mirage 2000 D',
    'ATLA': 'Breguet Atlantique ATL2',
    'FA10': 'Dassault Falcon 10 MER',
    'E2': 'E-2D Hawkeye',
    'FTCL': 'Flight Design CTLS',
    'SM19': 'SIAI-Marchetti SM.1019 E',
    'DUOD': 'Schempp-Hirth Duo Discus T',
    'VENT': 'Schempp-Hirth Ventus 2c T',
    'GLID': 'Schempp-Hirth Discus 2c',
    'AS16': 'Schleicher ASK 16',
    'DIMO': 'Diamond HK 36TTC 115 Super Dimona',
    'DG80': 'Glaser-Dirks DG-800B',
    'DISC': 'Schempp-Hirth Discus bT',
    'ARCP': 'Schempp-Hirth Arcus T',
    'G109': 'Grob G 109B',
    'SF25': 'Scheibe SF-25C Falke 2000',
    'RF5': 'Sportavia-Putzer RF-5B Sperber',
    'AV68': 'Alpla Samburo AVo-68 V',
    'EUFI': 'Eurofighter Typhoon',
    'HK36': 'HOAC HK-36R Super Dimona',
    'TFUN': 'Valentin Taifun 17E-II',
    'BALL': 'Google Loon Balloon',
    'GL5T': 'Bombardier Global 5000',
    'B105': 'MBB Bo.105 P',
    'F4': 'McDonnell Douglas F-4F Phantom II',
    'A321': 'Airbus A321 231',
    'H145M': 'Airbus H145M',
    'UH1': 'Bell UH-1N Iroquois',
    'H53': 'Sikorsky MH-53E Sea Dragon',
    'S61': 'Westland Sea King HC.4',
    '-TWR': 'Tower',
    'SH36': 'Short SD3-60 200',
    'F27': 'Fokker F-27  Troopship',
    'G115': 'Grob G-115 E Tutor',
    'B212': 'Bell 212',
    'FURY': 'Hawker Sea Fury FB.11',
    'DA42': 'Diamond Aircraft Twin Star DA42',
    'S92': 'Sikorsky CH-148 (S-92 Cyclone)',
    'DHC2': 'U-6A Beaver (DHC-2)',
    'AUS9': 'Auster Aircraft Auster B.5 AOP.9',
    'E50P': 'Embraer Phenom 100 U-100',
    'JPRO': 'British Aircraft Corporation Jet Provost T.5A',
    'DHC1': 'De Havilland DHC-1 Chipmunk T.10',
    'H64': ' Boeing AH-64E Apache Guardian',
    'HAWK': 'McDonnell Douglas T-45C Goshawk',
    'BN2T': 'Britten-Norman BN-2T-4S Defender 4000',
    'B461': 'BAe 146 CC.2',
    'A748': 'HAL.748 102',
    'HUNT': 'Hawker Hunter MK.58\t',
    'RJ70': 'Avro 146 RJ70',
    'SWOR': 'Fairey Swordfish II',
    'SHAW': 'Armstrong Whitworth Sea Hawk FGA.6',
    'ZZZZ': 'Embraer',
    'R135': 'Boeing TC-135W Stratolifter',
    'DC3': '1944 DOUGLAS DC3C-S4C4G',
    'HURI': 'Hawker Hurricane',
    'LANC': 'Avro Lancaster B.I',
    'SPIT': 'Vickers Supermarine Spitfire LF.IXc',
    'TUCA': 'Embraer EMB.312 Tucano T-27',
    'PA31': 'PA-31-310 Navajo',
    'T6': 'Noorduyn AT-16ND Harvard IIB',
    'B462': 'BAe 146 200',
    'F35': 'Lockheed Martin F-35 Lightning II',
    'TYPH': 'Eurofighter Typhoon T.3',
    'G12T': 'G-120TP',
    'P8': 'Boeing P-8A Poseidon',
    'PA32': 'Piper PA-32 301XTC Piper 6XT',
    'PA30': 'Piper PA-39 Twin Comanche C/R',
    'C510': 'Cessna Citation Mustang',
    'C421': 'Cessna 421C Golden Eagle',
    'B772': 'Boeing 777 2ANER',
    'AT75': 'Avions de Transport Regional ATR 72 500',
    'EA50': 'Eclipse Aviation EA500',
    'PA34': 'Embraer Seneca Emb-810',
    'P32R': 'Piper PA-32R 301T Turbo Saratoga SP',
    'B721': 'Boeing 727 76/W',
    'E190': 'Embraer EMB-190 VC-2',
    'B734': 'Boeing 737 4U3',
    'C310': 'Cessna 310Q',
    'BE58': 'Raytheon Aircraft Baron G58',
    'BE55': '1965 BEECH 95-B55 (T42A)',
    'C550': 'Cessna Citation II',
    'B735': 'Boeing 737 528',
    'TBM9': 'DAHER-SOCATA TBM 930',
    'JS31': 'British Aerospace Jetstream 31-12',
    'AT42': 'ATR 42-300',
    'SF50': 'Cirrus Jet Vision SF50',
    'B773': 'Boeing 777 35RER',
    'DA62': 'Diamond Aircraft DA62',
    'CRJ2': 'Dornier C-146A Wolfhound',
    'B206': 'Bell 206B Jet Ranger III',
    'ALO2': 'Sud Aviation Alouette II SE.3130',
    'G300': 'Gulfstream Aerospace G300',
    'C25M': 'Textron Aviation Citation M2',
    'A346': 'Airbus A340ACJ 642X',
    'S22T': 'Cirrus Design SR22T',
    'H': 'Socata TB-20 Trinidad',
    'TB20': ' SOCATA TB-20 TRINIDAD',
    'LAMA': 'Aerospatiale Lama SA.315B',
    'P46T': 'Piper PA-46 JetPROP',
    'P28B': 'Piper PA-28 236 Dakota',
    'BE36': 'Raytheon Aircraft Bonanza G36',
    'A330': 'Airbus A330-203',
    'E55P': 'EMB-505 Phenom 300',
    'C335': 'Cessna 335',
    'B505': 'Bell 505 Jet Ranger X',
    'PA46': 'Piper PA-46 350P Malibu Mirage',
    'R66': 'Robinson R66',
    'A333': 'Airbus A330 322',
    'BN2P': 'Britten-Norman Islander BN-2A-21',
    'DA40': 'Diamond Aircraft Diamond Star DA40',
    'TBM8': 'DAHER-SOCATA TBM 850',
    'E550': 'Embraer Legacy 500 IU-50',
    'C25C': 'Textron Aviation Citation CJ4',
    'EXPL': 'MD Helicopters MD 900 Explorer',
    'ULAC': 'Zlin Aviation Shock Cub',
    'PC7': 'Pilatus PC-7',
    'H60': 'Sikorsky UH-60M Black Hawk',
    'C182': 'Cessna 182E Skylane',
    'MD52': 'McDonnell Douglas Helicopters MD 520N',
    'ALO3': 'Sud Aviation Alouette III SA.316',
    'UAV': 'Northrop Grumman MQ-4C Triton',
    'E135': 'Embraer ERJ-135 VC-99C',
    'PA18': 'Piper PA-18 L-21C Super Cub',
    'MI8': 'Mil Mi-17 1V',
    'H500': 'Hughes 369 MD',
    'F260': 'SIAI-Marchetti SF.260 EU',
    'PC9': 'Pilatus PC-9',
    'LJ35': 'Gates Learjet 35 A',
    'PA36': 'Piper PA-36 375 Pawnee Brave',
    'M18': 'Pzl-Mielec Dromader M-18',
    'MG29': 'Mikoyan Gurevich MiG-29 G',
    'AN26': 'Antonov An-26 B',
    'AS3B': 'Eurocopter Cougar AS.532 U2',
    'SB39': 'SAAB Gripen JAS-39 C',
    'YK52': 'Aerostar Yak-52',
    'M7': 'Maule M-7 235 Super Rocket',
    'MF17': 'SAAB MFI-15',
    'H269': 'Schweizer 269 TH-300C',
    'VAMP': 'FFA Vampire T.55',
    'F70/C172': 'Fokker 70/Cessna 172 Skyhawk',
    'SF34': 'SAAB 340 B',
    'DC10': 'Douglas KC-10A Extender',
    'F50': 'Fokker F50 604UTA',
    'B77L': 'Boeing 777 200LR',
    'C172': 'Cessna 172S Skyhawk SP',
    'BE18': 'Beech Expeditor 3NM',
    'S11': 'Fokker Instructor S.11',
    'B25': 'B-25J-30-NC  "Devil Dog"',
    'AN28': 'PZL-Mielec M-28TD Bryza-1',
    'M28': 'PZL C-145A Skytruck (M28-05)',
    'C402': 'Cessna 402C',
    'PZ3T': 'PZL-130 TC2 Orlik',
    'A119': 'AgustaWestland Philadelphia AW.119 MkII',
    'YK40': 'Yakovlev Yak-40',
    'SB35': 'SAAB Draken J-35J',
    'JAS39': 'SAAB JAS-39C Gripen ',
    'C210': 'Cessna 210D Centurion',
    'W3': 'Pzl-Swidnik Sokol W-3 T',
    'MI2': 'Mil Mi-2 RS',
    'L159': 'Aero Vodochody L-159 A',
    'MI24': 'Mil Mi-24 V',
    'C152': 'Cessna 152',
    'Z42': 'Moravan Zlin Z-242 L',
    'EN48': 'Enstrom 480 B',
    'MI8?': 'Enstrom 480 B',
    'L39': 'Aero Vodochody L-39 NG',
    'Z26': 'Moravan Zlin Akrobat Z-526AFS',
    'Z37P': 'Let Cmelak Z-37A',
    'PAY3': 'Piper PA-42 Cheyenne III',
    'SBR1': 'North American T-39N Sabreliner',
    'SB05': 'SAAB 105 Sk-60E MT',
    'SB37': 'SAAB Viggen Sk-37E',
    'SB32': 'SAAB Lansen J-32D',
    'F18': 'Boeing F/A-18F Super Hornet',
    'E737': 'Boeing E-7A Wedgetail',
    'A318': 'Airbus ACJ318 112 Elite',
    'S76': 'Sikorsky S-76 A',
    'C337': 'Cessna O-2A',
    'LJ45': 'Bombardier Learjet 45 XR',
    'AT8T': 'Air Tractor AT-802',
    'AN2': 'Antonov An-2 R',
    'Z43': 'Moravan Zlin Z-143 L',
    'PIPA': 'Pipistrel Panthera',
    'WT9': 'Aerospool WT9 Dynamic',
    'EV97': 'Evektor-Aerotechnik EV-97 Eurostar SL',
    'PIAT': 'Pipistrel Alpha Trainer',
    'B763': 'Boeing 767 3Y0ER',
    'C500': 'Cessna Citation I',
    'C525': 'Cessna Citation CJ1',
    'SW4': 'Swearingen C-26A Metro',
    'CRJ7': 'Bombardier Challenger 870',
    'YK42': 'Yakovlev Yak-42 D',
    'B300': 'Raytheon MC-12S-1 Emarss-G 4',
    'AN32': 'Antonov An-32 RE',
    'B739': 'Boeing 737NG 9BQ BBJ3',
    'MA60': 'Xian MA60 Y7G',
    'BA11': 'British Aircraft Corp One-Eleven 485GD',
    'C55B': 'Cessna Citation Bravo',
    'SB20': 'SAAB 2000 AEW',
    'B742': 'Boeing E-4B Night Watch',
    'C180': '1954 CESSNA 180',
    'EC20': 'Eurocopter EC120B',
    'G280': 'Gulfstream Aerospace G280',
    'BE40': '400A',
    'C185': 'Cessna 185A Skywagon',
    'EC55': 'Eurocopter EC155 B1',
    'EC75': 'Airbus Helicopters EC175 B (H175)',
    'Y20': 'Xian Y-20 A',
    'NNJA': 'Best Off Nynja',
    'CH60': 'Zenair CH601XLB Zodiac',
    'MAGC': 'Ibis Magic GS700',
    'ALIG': 'Arion Lightning',
    'ZEPH': 'ATEC Zephyr',
    'SVNH': 'ICP MXP-740 Savannah',
    'JAB4': 'Jabiru J230-D',
    'BR60': 'Brumby 600',
    'EFOX': 'Aeropro Eurofox 3K Trigear 100ULS',
    'PIVI': 'Pipistrel Virus SW',
    'AP22': 'Aeroprakt A22LS Foxbat\xa0',
    'ECHO': 'Tecnam P92 Echo Classic',
    'FDCT': 'Flight Design CTLS',
    'SLG2': 'Airplane Factory Sling 2',
    'JAB2': 'Jabiru J160-D',
    'NG5': 'BRM Aero Bristell RG',
    'PISI': 'Pipistrel Sinus 912 Flex',
    'P208': 'Tecnam P.2008',
    'SYNC': 'Fly Synthesis Syncro',
    'TL20': 'TL-2000 Sting Carbon S4',
    'AP32': 'Aeroprakt A-32 Vixxen',
    'BR61': 'Brumby LSA-R610 Evolution',
    'FAET': 'ATEC 321 Faeta NG',
    'PIAE': 'Pipistrel Alpha Electro',
    'SIRA': 'Tecnam P2002 Sierra Mk II',
    'PNR2': 'Alpi Pioneer 200',
    'SAVG': 'Zlin Savage Shock Cub',
    'L8': 'Luscombe Silvaire 8E',
    'VL3/L8': 'JMB VL-3 Evolution/Luscombe 8E Silvaire',
    'TL30': 'TL-3000 Sirius',
    'JABI': 'Jabiru Aircraft Jabiru LSA 2J',
    'B06': 'Agusta-Bell AB.206 Jet Ranger B-1',
    'KC3': 'Airbus KC-30A ',
    'B350?': 'Boeing-McDonnell Douglas AH-64D Apache',
    'B77W': 'Boeing 777 300ER',
    'P1': 'Kawasaki P-1',
    'KC2': 'Kawasaki C-2',
    'C68A': 'Textron Aviation U-680A',
    'JS41': 'British Aerospace Jetstream 41 -22',
    'SU95': 'Sukhoi Superjet 100 95 VIP',
    'B430': 'Bell 430',
    'RJ85': 'Avro 146 RJ85',
    'B764': 'Boeing 767 4FSER',
    'B789': 'Boeing 787-9',
    'KODI': 'Quest Aircraft Company Kodiak 100',
    'KT1': 'KAI KT-1 Wong Bee B',
    'E6': 'Boeing E-6B Mercury',
    'P28R': '1974 PIPER PA-28R-200',
    'E120': 'Embraer EMB-120 C-97',
    'P-3': 'Lockheed P-3B',
    'SHIP': ' AMERICAN BLIMP CORP A-1-70G',
    'DHC7': 'De Havilland Canada TO-5C (RC-7B) DHC-7',
    'C82R': '1977 CESSNA R182',
    'D328': 'Dornier C-146A',
    'C170': '1948 CESSNA 170',
    'B736': '2001 BOEING 737-66N',
    'C77R': '1975 CESSNA 177RG',
    'P28A': '1981 PIPER PA-28-161',
    'B17': '1944 BOEING B-17G',
    'KFIR': 'IAI Kfir-C2',
    'T34P': '1955 BEECH D-45',
    'TBM': 'Grumman TBM-3 "Doris Mae"',
    'B407': 'Bell 407 GX',
    'DG1T': ' DG FLUGZEUGBAU GMBH DG 1000S',
    'C150': 'Cessna 150M',
    'MRF1': 'Dassault Mirage F.1 M',
    'MD60': 'MD Helicopters MD 600N',
    'PA27': '1968 PIPER PA-23-250',
    'E762': 'Boeing E-767 AWACS',
    'P28T': '1980 PIPER PA-28RT-201',
    'RF10': 'Aeromot AMT-200S TG-14A Super Ximango',
    'F18H': 'McDonnell Douglas F/A-18C Hornet',
    'DC93': 'Douglas C-9B Skytrain II',
    'T38': 'Northrop Grumman T-38C Talon',
    'KC10': 'Douglas KC-10A Extender',
    'T33': 'T-38C',
    'T68': 'T-38C',
    'ASTR': 'C-38A',
    'C32': 'C-32B',
    'C2': 'Grumman C-2A Greyhound',
    'K35E': 'Boeing KC-135E',
    'B737/K35R': 'Boeing C-40A Clipper/KC-135R',
    'K35R/C12': 'Boeing KC-135R/C-12U Huron',
    'C5M': 'Lockheed C-5M Galaxy',
    'C5': 'Lockheed C-5B Galaxy',
    'C5A': 'Lockheed C-5A Galaxy',
    'F15': 'McDonnell Douglas F-15E Strike Eagle',
    'F18S': 'Boeing F/A-18F Super Hornet',
    'U2': 'Lockheed U-2S',
    'E3TF/B350': 'Boeing E-3B Sentry/Beechcraft MC-12S',
    'E3CF/B350': 'Boeing E-3B Sentry/Beechcraft MC-12S',
    'E3TF': 'Boeing E-3G Sentry\t(AWACS)',
    'A6': 'Boeing EA-18G Growler',
    'TEX2?': 'Raytheon Aircraft Company T-6B Texan II',
    'V22': 'Bell-Boeing CV-22B Osprey',
    'SUCO': 'Bell AH-1Z Viper',
    'UH1Y': 'Bell Textron UH-1Y Venom',
    'A10': 'Fairchild A-10C Thunderbolt II',
    'P#': 'P-3',
    'H72': 'UH-72A',
    'DH8A': 'DHC-8-102 CT-142 Dash 8',
    'C12': 'Beechcraft C-12 Huron',
    'C27': 'Alenia C-27J Spartan',
    'C40': 'Boeing C-40A',
    'H60/CN35': 'Sikorsky MH-60R Seahawk',
    'PRED': 'General Atomics MQ-9 ',
    'MQ9': 'General Atomics MQ-9 ',
    'Q9': 'General Atomics MQ-9B Multi-Role Variant',
    'F1S': 'Boeing EA-18G Growler',
    'CV22': 'MV-22B Osprey',
    'H53?': 'Sikorsky CH-53E Sea Stallion',
    'MQ8': 'Northrop-Grumman MQ-8B Fire Scout',
    'V10': 'North American OV-10G+ Bronco',
    'Q4': 'Northrop Grumman MQ-4C Triton',
    'B52': 'B-52H',
    'A29': 'A-29B Super Tucano',
    'E314': 'Embraer EMB.314 Super Tucano A-29B',
    'DHC8': 'DeHavilland RO-6A ',
    'DHC3': 'de Havilland Canada DHC-3 Otter',
    'T34T': 'Beech T-34C Turbo Mentor',
    'T34': 'Beech T-34C Turbo Mentor',
    'H65': 'HH-65C',
    'MD88': 'McDonnell Douglas DC-9 88',
    'SONX': 'Sonex Sonex',
    'A4': 'Douglas A-4N Skyhawk',
    'CL-60': 'CC-144',
    'CC144': 'Bombardier CC-144D',
    'H25A': 'British Aerospace 125 700A',
    'LJ55': 'Gates Learjet 55 C',
    'E545': 'Embraer Legacy 450',
    'KC39': 'Embraer KC-390',
    'A20N': 'Airbus A320 271NSL',
    'FA5X': 'Dassault Falcon 50EX'
}

HEX_LOOKUP = {
    "400EFC": MODEL['A319'],
    "4074E2": MODEL['B788'],
    "48506B": MODEL['B788'],
    "4CA63A": MODEL['A320'],
    "40641D": MODEL['A333'],
    "406A95": MODEL['A320'],
    "424B6B": MODEL['GL7T'],
    "A83F8C": MODEL['B748'],
    "4CA15D": MODEL['A320'],
    "43C922": MODEL['TEX2'],
    "43C921": MODEL['TEX2'],
    "43C8CA": MODEL['TEX2'],
    "43C8CE": MODEL['TEX2'],
}

F15_CODES = [
    'AE1789',
    'AE178F',
    'AE17A3',
    'AE56E9',
    'AE1CBD',
    'AE1CC1',
    'AE1CC3',
    'AE1CC4',
    'AE1CC5',
    'AE2817',
    'AE1CC7',
    'AE1CC8',
    'AE1CC9',
    'AE1CCA',
    'AE2863',
    'AE1CCB',
    'AE1CCC',
    'AE1CCD',
    'AE1CCE',
    'AE1CD0',
    'AE1CD1',
    'AE1CD2',
    'AE1CD3',
    'AE1CD4',
    'AE1CD5',
    'AE17A4',
    'AE17A5',
    'AE17A6',
    'AE178A',
    'AE17A8',
    'AE17A9',
    'AE17AA',
    'AE17AB',
    'AE17AC',
    'AE179B',
    'AE1798',
    'AE178C',
    'AE1793',
    'AE179E',
    'AE17AD',
    'AE179F',
    'AE17A0',
    'AE1788',
    'AE17AE',
    'AE17A1',
    'AE17A2',
    'AE178D',
    'AE179A',
    'AE17B1',
    'AE17B2',
    'AE17B3',
    'AE17B4',
    'AE17B7',
    'AE17B8',
    'AE17B9',
    'AE17BA',
    'AE17BB',
    'AE17BC',
    'AE17BD',
    'AE17BE',
    'AE17BF',
    'AE56E7',
    'AE56E7',
    'AE071C',
    'AE17AF',
    'AE2DF7',
    'AE1790',
    'AE17B6',
    'AE1799',
    'AE179C',
    'AE5BC9',
    'AE1780',
    'AE17B0',
    'AE178E',
    'AE1791',
    'AE1796',
    'AE179D',
    'AE1792',
    'AE1797',
    'AE1795',
]

for code in F15_CODES:
    HEX_LOOKUP[code] = "F15"

HAWK_CODES = [
'70C0D1',
'70C0D2',
'165484',
'AE1103',
'70C0D4',
'167079',
'AE08AE',
'167085',
'AE08B4',
'167088',
'AE08B7',
'71036C',
'71036F',
'710370',
'710372',
'710374',
'71037B',
'A27-10',
'7CF854',
'A27-21',
'7CF855',
'43C5C1',
'43C0DC',
'43C0DD',
'43C0DE',
'43C0DF',
'43C0E2',
'43C0E7',
'43C0EE',
'43C0F3',
'43C0F5',
'43C0F6',
'43C0F7',
'43C0F9',
'43C400',
'43C403',
'43C404',
'43C405',
'43C406',
'43C407',
'43C408',
'43C409',
'43C40A',
'43C40B',
'43C40C',
'43C40D',
'43C40F',
'43C414',
'43C416',
'43C418',
'43C41C',
'43C41F',
'43C420',
'43C421',
'43C421',
'43C422',
'43C423',
'43C424',
'43C428',
'43C42B',
'43C42C',
'43C42D',
'43C42F',
'43C430',
'43C431',
'43C433',
'43C435',
'43C436',
'43C439',
'43C43B',
'43C443',
'43C444',
'43C44A',
'43C44B',
'43C44F',
'43C450',
'43C451',
'43C452',
'43C453',
'43C455',
'43C456',
'43C457',
'43C458',
'43C459',
'43C45B',
'43C45C',
'43C45D',
'43C45F',
'43C461',
'43C462',
'43C463',
'43C5C2',
'43C5C3',
'43C464',
'43C465',
'43C466',
'43C468',
'71036A',
'710378',
'710379',
'710371',
'43C098',
'43C04D',
'43C47A',
'43C47B',
'43C47C',
'43C54F',
'43C550',
'43C551',
'43C552',
'43C553',
'43C554',
'43C555',
'43C556',
'43C557',
'43C558',
'43C559',
'43C55A',
'43C55B',
'43C55C',
'43C55D',
'43C55E',
'43C55F',
'43C560',
'43C561',
'43C562',
'43C563',
'43C564',
'43C565',
'43C566',
'43C567',
'43C568',
]

for code in HAWK_CODES:
    HEX_LOOKUP[code] = MODEL["HAWK"]

with open("codes.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        HEX_LOOKUP[row[0]] = MODEL[row[1]]
