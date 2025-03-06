from enum import Enum

class StudentStatusState(Enum):
    TERDAFTAR = "Terdaftar"
    AKTIF = "Aktif"
    LULUS = "Lulus"
    CUTI = "Cuti"

class TriggerInputState(Enum):
    CETAK_KSM = "Cetak KSM"
    MENGAJUKAN_CUTI = "Mengajukan Cuti"
    LULUS = "Lulus"
    MENYELESAIKAN_CUTI = "Menyelesaikan Cuti"
    
transitions = {
    StudentStatusState.TERDAFTAR: {
        TriggerInputState.CETAK_KSM: StudentStatusState.AKTIF,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI,
    },
    StudentStatusState.AKTIF: {
        TriggerInputState.LULUS: StudentStatusState.LULUS,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI,
    },
    StudentStatusState.CUTI: {
        TriggerInputState.MENYELESAIKAN_CUTI: StudentStatusState.TERDAFTAR,
    },
}

def change_state(current_state, trigger_input):
    if current_state  in transitions and trigger_input in transitions[current_state]:
        return transitions[current_state][trigger_input]
    return "Transisi tidak valid"
    

current_state = StudentStatusState.TERDAFTAR
next_state = change_state(current_state, TriggerInputState.CETAK_KSM)
print(f"Next State => {next_state}")
next_state = change_state(current_state, TriggerInputState.LULUS)
print(f"Next State => {next_state}")

# Current State => StudentStatusState.AKTIF
# Trigger Input => TriggerInputState.MENGAJUKAN_CUTI
# Next State => Cuti

# Current State => StudenStatusState.CUTI
# Trigger Input => TriggerInputState.LULUS
# Next State => Transisi tidak valid