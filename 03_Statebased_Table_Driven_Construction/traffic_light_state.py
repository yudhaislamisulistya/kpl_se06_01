from enum import Enum
import time
# Bagian dari State
class TrafficLightState(Enum):
    MERAH = "Merah"
    HIJAU = "Hijau"
    KUNING = "Kuning"

# Bagian dari Transition atau Perubahan State
state_transitions = {
    TrafficLightState.MERAH: TrafficLightState.HIJAU,
    TrafficLightState.HIJAU: TrafficLightState.KUNING,
    TrafficLightState.KUNING: TrafficLightState.MERAH,
}

state_durations = {
    TrafficLightState.MERAH: 5,
    TrafficLightState.HIJAU: 10,
    TrafficLightState.KUNING: 2,
}

current_state = TrafficLightState.MERAH
# next_state = state_transitions[current_state]
# print(f"Next State: {next_state}")

while True:
    print(f"Lampu: {current_state.value} ({state_durations[current_state]} detik)")
    time.sleep(state_durations[current_state])
    current_state = state_transitions[current_state]
    print(f"Next State: {current_state.value}")
    print("")
    
    
