To run this code, we first need tiny_tamp:

```
git clone https://github.com/aidan-curtis/tiny_tamp
cd tiny_tamp
python -m pip install -e .
cd ..
git clone https://github.com/chsahit/panda_vis_pb
```

Then to visualize, make make sure that `traj.pkl` stores a list of 7-dimensional lists (corresponding to joint angles). Then run `python vis.py`
