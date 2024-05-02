class System:
    dT = 0.01
    dt = 0.00001
    mu = 0.05

    def __init__(self) -> None:
        # the list of all the states the system has been in
        self.history = np.ndarray(dtype=State)

    def run(self, steps: int) -> None:
        for T in range(steps):
            temp_state = self.history[-1].get_next(self.dT)

            if not temp_state.has_overlap():
                # no collision, we're good
                self.history.append(temp_state)
            else:
                # collision detected
                for t in range(self.dT / self.dt):
                    temp_state = self.history[-1].get_next(self.dt)
                    if temp_state.has_overlap():
                        self.history[-1].deal_with_overlap()
            
