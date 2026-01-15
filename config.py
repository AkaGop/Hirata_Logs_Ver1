# config.py
"""
Single source of truth for all static configuration data.
Includes the COMPLETE alarm code mapping from the specification document.
"""

CEID_MAP = {
    # GEM Events
    7: "GemOpCommand", 11: "Equipment Offline", 12: "Control State Local", 13: "Control State Remote",
    14: "GemMsgRecognition", 16: "PP-SELECT Changed", 30: "Process State Change",
    101: "Alarm Cleared", 102: "Alarm Set",

    # Custom/Alarm related CEIDs found in logs
    18: "AlarmSet", 113: "AlarmSet", 114: "AlarmSet",

    # Equipment Inherent Events
    120: "IDRead", 121: "UnloadedFromMag", 122: "LoadedToMag", 126: "UnloadedFromTool",
    127: "LoadedToTool", 128: "PP-Selected", 131: "LoadToToolCompleted", 132: "UnloadFromToolCompleted",
    133: "MagToMagCompleted", 134: "MagCheckedCompleted", 136: "MappingCompleted",
    141: "PortStatusChange",
    151: "LoadStarted",  # Corrected Mapping
    180: "RequestMagazineDock", 181: "MagazineDocked", 182: "MagazineUndocked",
    183: "RequestOperatorIdCheck", 184: "RequestOperatorLogin", 185: "RequestMappingCheck",
}

RPTID_MAP = {
    8: ['OperatorCommand'], 11: ['ControlState'], 14: ['Clock'], 16: ['PPChangeName', 'PPChangeStatus'],
    32: ['ProcessState', 'PreviousProcessState'], 101:['Clock', 'AlarmID'],
    120: ['LotID', 'PanelID', 'Orientation', 'ResultCode', 'SlotID'],
    121: ['LotID', 'PanelID', 'SourcePortID'], 141: ['PortID', 'PortStatus'],
    150: ['MagazineID'], 151: ['PortID', 'MagazineID', 'OperatorID'], 152: ['OperatorID'],
}

# --- COMPLETE ALARM DATABASE ---
ALARM_DB = {
    1: {'description': '<0001>CPU error', 'level': 'Error'}, 2: {'description': '<0002>SafetyPLC error', 'level': 'Error'},
    9: {'description': '<0051>EtherNet/IP error', 'level': 'Error'},
    # Add your complete ALARM_DB dictionary here...
}
