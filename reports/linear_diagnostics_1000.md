\# Linear Regression Diagnostics



\## Figure References



Figure 1: Residuals vs Predicted Yield



Figure 2: Residuals vs Humidity



\## Residual Analysis



Residuals were calculated as:



Residual = Actual Yield − Predicted Yield



The residual plots were examined to determine whether prediction errors behaved randomly or exhibited systematic patterns.



The residuals appeared reasonably centered around zero with no major clustering. No severe funnel-shaped pattern was observed, suggesting that heteroscedasticity is limited.



The residuals versus humidity plot did not reveal strong nonlinear structure. Any observed curvature was minor and does not significantly affect predictive performance.



A small number of larger residuals were observed. These may correspond to unusual growing conditions, data recording variation, or special operational events.



\## Recommendation



The Linear Regression model achieved strong predictive performance with an R² score of 0.870.



The residual diagnostics do not reveal major violations of model assumptions. Therefore, Linear Regression remains a useful baseline model.



However, Random Forest Regression should be explored in the next phase because it can capture nonlinear relationships and feature interactions that linear models cannot represent.



