import mujoco
spec = mujoco.MjSpec()
spec.modelname = "my model"
body = spec.worldbody.add_body(
    pos=[1, 2, 3],
    quat=[0, 1, 0, 0],
)
geom = body.add_geom(
    name='my_geom',
    type=mujoco.mjtGeom.mjGEOM_SPHERE,
    size=[1, 0, 0],
    rgba=[1, 0, 0, 1],
)
...
model = spec.compile()