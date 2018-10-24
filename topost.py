config = {
    'noise_params': {
        'relaxation_rate': 1/50, #us
        'thermal_populations': [0.99, 0.01],
        'CX': {'gate_time': 0.1},
        'U': {'p_pauli': [0.01, 0, 0],'gate_time': 1}
    }
}

beta=pi/2+pi/2
gamma=0.5  
config1 = {
    'noise_params': {
        'CX': {"calibration_error": beta,"zz_error": gamma}
    }
}
sim = 'qasm_simulator'

job = execute(twoQubitRB,Aer.get_backend(sim))
result = job.result()
count=result.get_counts()


job = execute(twoQubitRB,Aer.get_backend(sim), config)
result = job.result()
count1=result.get_counts()

job = execute(twoQubitRB,Aer.get_backend(sim),config=config1)
result = job.result()
count2=result.get_counts()

print(count)
print(count1)
print(count2)