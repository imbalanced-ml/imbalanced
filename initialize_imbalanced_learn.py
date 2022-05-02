def launch_imbalanced_learn():
    class FakeRandom:
        def __init__(self):
            pass

        def randn(self):
            return 0.

    class FakeNumpy:
        def __init__(self):
            self.random = FakeRandom()

    import sys
    del sys.modules['numpy']
    sys.modules['numpy'] = FakeNumpy()
