import logging 
import mne

channel_mapping_10_20 = {
    "EEG001": "Fp1", "EEG002": "F3", "EEG003": "F7", "EEG004": "C3", "EEG005": "P3",
    "EEG006": "O1", "EEG007": "T3", "EEG008": "T5", "EEG009": "Fz", "EEG010": "Pz",
    "EEG011": "FC1", "EEG012": "CP1", "EEG013": "FC5", "EEG014": "CP5", "EEG015": "AF3",
    "EEG016": "PO3", "EEG017": "Fp1", "EEG018": "F3", "EEG019": "F7", "EEG020": "C3",
    "EEG021": "P3", "EEG022": "O1", "EEG023": "T3", "EEG024": "T5", "EEG025": "Fz",
    "EEG026": "Pz", "EEG027": "FC1", "EEG028": "CP1", "EEG029": "FC5", "EEG030": "CP5",
    "EEG031": "AF3", "EEG032": "PO3", "EEG033": "Fp2", "EEG034": "F4", "EEG035": "F8",
    "EEG036": "C4", "EEG037": "P4", "EEG038": "O2", "EEG039": "T4", "EEG040": "T6",
    "EEG041": "Cz", "EEG042": "Oz", "EEG043": "FC2", "EEG044": "CP2", "EEG045": "FC6",
    "EEG046": "CP6", "EEG047": "AF4", "EEG048": "PO4", "EEG049": "Fp2", "EEG050": "F4",
    "EEG051": "F8", "EEG052": "C4", "EEG053": "P4", "EEG054": "O2", "EEG055": "T4",
    "EEG056": "T6", "EEG057": "Cz", "EEG058": "Oz", "EEG059": "FC2", "EEG060": "CP2",
    "EEG061": "FC6", "EEG062": "CP6", "EEG063": "AF4", "EEG064": "PO4"
}

channel_mapping_10_10 = {
    "EEG001": "AF7", "EEG002": "AF8", "EEG003": "F7", "EEG004": "F8", "EEG005": "FC5", 
    "EEG006": "FC6", "EEG007": "FC1", "EEG008": "Fpz", "EEG009": "C5", "EEG010": "C6", 
    "EEG011": "CP5", "EEG012": "CP6", "EEG013": "P7", "EEG014": "P8", "EEG015": "Oz", 
    "EEG016": "Iz", "EEG017": "T5", "EEG018": "T6", "EEG019": "POz", "EEG020": "PO5"
}

channel_mapping_10_5 = {
    'EEG001': 'Fp1',
    'EEG002': 'AF7',
    'EEG003': 'AF3',
    'EEG004': 'F1',
    'EEG005': 'F3',
    'EEG006': 'F5',
    'EEG007': 'F7',
    'EEG008': 'FT7',
    'EEG009': 'FC5',
    'EEG010': 'FC3',
    'EEG011': 'FC1',
    'EEG012': 'C1',
    'EEG013': 'C3',
    'EEG014': 'C5',
    'EEG015': 'T7',
    'EEG016': 'TP7',
    'EEG017': 'CP5',
    'EEG018': 'CP3',
    'EEG019': 'CP1',
    'EEG020': 'P1',
    'EEG021': 'P3',
    'EEG022': 'P5',
    'EEG023': 'P7',
    'EEG024': 'PO7',
    'EEG025': 'PO3',
    'EEG026': 'O1',
    'EEG027': 'Oz',
    'EEG028': 'O2',
    'EEG029': 'PO4',
    'EEG030': 'PO8',
    'EEG031': 'P8',
    'EEG032': 'P6',
    'EEG033': 'P4',
    'EEG034': 'P2',
    'EEG035': 'CP2',
    'EEG036': 'CP4',
    'EEG037': 'CP6',
    'EEG038': 'TP8',
    'EEG039': 'T8',
    'EEG040': 'C6',
    'EEG041': 'C4',
    'EEG042': 'C2',
    'EEG043': 'CP0',
    'EEG044': 'CP3',
    'EEG045': 'CP5',
    'EEG046': 'TP7',
    'EEG047': 'T7',
    'EEG048': 'C5',
    'EEG049': 'C3',
    'EEG050': 'C1',
    'EEG051': 'FC1',
    'EEG052': 'FC3',
    'EEG053': 'FC5',
    'EEG054': 'FT7',
    'EEG055': 'F7',
    'EEG056': 'F5',
    'EEG057': 'F3',
    'EEG058': 'F1',
    'EEG059': 'AF3',
    'EEG060': 'AF7',
    'EEG061': 'Fp1',
    'EEG062': 'Fpz',
    'EEG063': 'Fz',
    'EEG064': 'Cz',
    # Continue up to 'EEG128' as needed
}

channel_mapping_biosemi64 = {
    'EEG001': 'Fp1',
    'EEG002': 'AF7',
    'EEG003': 'AF3',
    'EEG004': 'F1',
    'EEG005': 'F3',
    'EEG006': 'F5',
    'EEG007': 'F7',
    'EEG008': 'FT7',
    'EEG009': 'FC5',
    'EEG010': 'FC3',
    'EEG011': 'FC1',
    'EEG012': 'C1',
    'EEG013': 'C3',
    'EEG014': 'C5',
    'EEG015': 'T7',
    'EEG016': 'TP7',
    'EEG017': 'CP5',
    'EEG018': 'CP3',
    'EEG019': 'CP1',
    'EEG020': 'P1',
    'EEG021': 'P3',
    'EEG022': 'P5',
    'EEG023': 'P7',
    'EEG024': 'PO7',
    'EEG025': 'PO3',
    'EEG026': 'O1',
    'EEG027': 'Oz',
    'EEG028': 'O2',
    'EEG029': 'PO4',
    'EEG030': 'PO8',
    'EEG031': 'P8',
    'EEG032': 'P6',
    'EEG033': 'P4',
    'EEG034': 'P2',
    'EEG035': 'CP2',
    'EEG036': 'CP4',
    'EEG037': 'CP6',
    'EEG038': 'TP8',
    'EEG039': 'T8',
    'EEG040': 'C6',
    'EEG041': 'C4',
    'EEG042': 'C2',
    'EEG043': 'CP0',
    'EEG044': 'CP3',
    'EEG045': 'CP5',
    'EEG046': 'TP7',
    'EEG047': 'T7',
    'EEG048': 'C5',
    'EEG049': 'C3',
    'EEG050': 'C1',
    'EEG051': 'FC1',
    'EEG052': 'FC3',
    'EEG053': 'FC5',
    'EEG054': 'FT7',
    'EEG055': 'F7',
    'EEG056': 'F5',
    'EEG057': 'F3',
    'EEG058': 'F1',
    'EEG059': 'AF3',
    'EEG060': 'AF7',
    'EEG061': 'Fp1',
    'EEG062': 'Fpz',
    'EEG063': 'Fz',
    'EEG064': 'Cz',
}

standards = {
    'standard_1020': channel_mapping_10_20,
    'standard_1010': channel_mapping_10_10,
    'standard_1005': channel_mapping_10_5,
    'biosemi64': channel_mapping_biosemi64, 
}

def get_channel_mapping(montage):
    return standards.get(montage, {})