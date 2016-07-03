[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

```python
from thinkstats2 import CohenEffectSize
from first import MakeFrames
live, firsts, others = first.MakeFrames()
cohens_d = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
print(cohens_d)
```

> Cohen's D = -0.08867, which suggests that the effect size of being first-born on baby weight is smaller than that on pregnancy length.