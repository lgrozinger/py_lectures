# for setting up
import setup_env

# for simulating
import tellurium as te

# for plotting
import matplotlib
matplotlib.use("TKAgg")

# load model from a file
with open("models/repressilator_modular.model") as model:
  r = te.loada(model.read())

# simulate from 0 to max_time, plotting every minute
max_time = 600.0
r.simulate(0, max_time, int(max_time))
# plot the simulation
r.plot()