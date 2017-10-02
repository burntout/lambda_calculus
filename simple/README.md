# Simple

This directory contains examples which don't require recursion.
This makes the lambda implementations simpler, because we don't need to take into account that Python is eager.
However, when we require recursion, the simple returns have to be wrapped in additional lambda's to prevent early execution
