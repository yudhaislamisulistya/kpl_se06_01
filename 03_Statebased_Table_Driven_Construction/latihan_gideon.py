from enum import Enum

class FsmState(Enum):
    IDLE = "Idle"
    MENUNGGU_PRODUK = "Menunggu Produk"
    MENGELUARKAN_PRODUK = "Mengeluarkan Produk"
    SELESAI = 'Selesai'

class StateTrigger(Enum):
    MASUKKAN_UANG = "Masukkan Uang"
    PILIH_PRODUK = "Pilih Produk"
    KELUARKAN_PRODUK = "Keluarkan Produk"
    RESET = "Reset"

state_transition = {
    FsmState.IDLE: {
        StateTrigger.MASUKKAN_UANG: FsmState.MENUNGGU_PRODUK
    },
    FsmState.MENGELUARKAN_PRODUK: {
        StateTrigger.PILIH_PRODUK: FsmState.MENGELUARKAN_PRODUK
    },
    FsmState.MENGELUARKAN_PRODUK: {
        StateTrigger.KELUARKAN_PRODUK: FsmState.SELESAI
    },
    FsmState.SELESAI: {
        StateTrigger.RESET: FsmState.IDLE
    }
}

def change_state(current_state, trigger_input):
    if (current_state in state_transition
        and trigger_input in state_transition[current_state]):
        return state_transition[current_state][trigger_input]

    return "transisi salah"

current_state = FsmState.IDLE
next_state = change_state(current_state, StateTrigger.MASUKKAN_UANG)
print(next_state)