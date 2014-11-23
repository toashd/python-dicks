import dicks

api = dicks.Client()

dicks = api.get_dicks()
print(dicks)

blacks = api.get_dicks(size='black')
print(blacks)

served = api.get_dicks_served()
print(served)

