from sklearn.linear_model import LinearRegression

class OrdinaryLeastSquaresRegression(LinearRegression):
    """
    Ordinary Least Squares Regression implementation.
    This is a wrapper around sklearn's LinearRegression which already implements OLS.
    """
    pass  # All functionality is inherited from sklearn's LinearRegression 