from pathlib import Path

SOLUTIONS = [
    (1, "B", r"Compute the sample mean: $(36 + 49.1 + 41.5 + 40 + 46.4)/5 = 42.6\,\text{kg}$."),
    (2, "E", r"Use the sample standard deviation with denominator $n-1$: $s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{4}} \approx 5.20\,\text{kg}$."),
    (3, "C", r"The measurements are quantitative on a continuum, so the data type is continuous."),
    (4, "A", r"The $65$ minutes is the observed sample mean from $n=764$ students, so it is a statistic and a realised value of a random variable."),
    (5, "C", r"The target population is all New Zealand high school students and the parameter is their mean weekly exercise time."),
    (6, "B", r"Treating 1989--2000 as 12 years, the incidence rate is $\frac{175}{1904\times 12}\times 100{,}000 \approx 7.66\times 10^2$ fractures per $100{,}000$ person-years, describing the study cohort."),
    (7, "B", r"The relative risk is $\big(175/(1904\times 12)\big)\big/\big(54/(1373\times 12)\big) \approx 2.34$."),
    (8, "D", r"Under-diagnosis of men makes the observed male rate too small, so the ratio $\text{rate}_\text{women}/\text{rate}_\text{men}$ is biased upward."),
    (9, "A", r"The quoted 4.5 and 1.9 values summarise the observed rate ratios in the study for the 60--69 and $80+$ age bands."),
    (10, "D", r"The mean of the total is $\mu_W = \mu_X + \mu_Y = 1750 + 750 = 2500$."),
    (11, "C", r"With independent counts, variances add: $\sigma_W = \sqrt{100^2 + 40^2} = \sqrt{11{,}600} \approx 1.08\times 10^2$."),
    (12, "C", r"$\Pr(B) = 82/623 \approx 0.1316$."),
    (13, "A", r"$\Pr(A^c \cap B) = 50/623 \approx 0.0803$."),
    (14, "E", r"$\Pr(A^c \mid B) = 50/82 \approx 0.610$."),
    (15, "B", r"Sensitivity is $\Pr(T\mid B) = 0.97$."),
    (16, "A", r"Specificity is $\Pr(T^c\mid B^c) = 1 - 0.35 = 0.65$."),
    (17, "B", r"$\Pr(B\cap T) = \Pr(B)\Pr(T\mid B) = 0.20\times 0.97 = 0.194$."),
    (18, "C", r"$\Pr(B^c \cap T) = 0.80\times 0.35 = 0.28$."),
    (19, "A", r"$\Pr(T) = 0.194 + 0.28 = 0.474 \approx 0.47$."),
    (20, "C", r"Positive predictive value $= 0.194/0.474 \approx 0.41$."),
    (21, "B", r"A binomial model requires a fixed $n$, identical success probability for each trial, independence, and two possible outcomes per trial."),
    (22, "C", r"From the table, $\Pr(X=3) = 0.0081$."),
    (23, "D", r"$\Pr(X>3) = \Pr(4) + \Pr(5) = 0.00045 + 0.00001 = 0.00046$."),
    (24, "D", r"Because 150 exceeds the mean of a symmetric normal distribution, the upper-tail probability must be between $0$ and $0.5$."),
    (25, "A", r"The upper tail is $1 - \operatorname{pnorm}(137.5,\ 127.5,\ 19.6)$."),
    (26, "B", r"The middle probability is $\operatorname{pnorm}(134.5, 127.5, 19.6) - \operatorname{pnorm}(119.5, 127.5, 19.6)$."),
    (27, "D", r"$z = (140.5 - 127.5)/19.6 \approx 0.66$."),
    (28, "B", r"Using $t_{0.975,194}$ with $s/\sqrt{n}$ constructs a 95\% confidence interval for the population mean BMI."),
    (29, "D", r"Using $z_{0.975}\,s$ without $\sqrt{n}$ gives an estimated 95\% reference range for individual BMIs."),
    (30, "C", r"The mean paired difference (after $-$ before) is $52.9 - 56.5 = -3.6$ bpm."),
    (31, "E", r"The estimated standard error is $s_d/\sqrt{n} = 5.9/\sqrt{13} \approx 1.64$ bpm."),
    (32, "A", r"For a 95\% interval with $n=13$, use $t_{0.975,12}$."),
    (33, "D", r"The 95\% CI for the population mean difference excludes zero and is entirely negative, so the data suggest a true decrease in resting heart rate among female runners following the protocol."),
    (34, "A", r"The sample proportion is $\hat{p} = 49/99 \approx 0.495$."),
    (35, "B", r"$\text{SE} = \sqrt{\hat{p}(1-\hat{p})/n} = \sqrt{0.495\times 0.505/99} \approx 0.050$."),
    (36, "B", r"A large-sample CI for a proportion uses $\hat{p} \pm z_{0.975}\,\text{SE}$."),
    (37, "C", r"The interval gives a 95\% confidence range for the population proportion of New Zealand adults whose main news source is mainstream media."),
    (38, "E", r"A valid normal approximation requires a large sample and success probability not too close to 0 or 1; $\hat{p}\approx 0.5$ satisfies this."),
    (39, "B", r"If mainstream-media users respond more, the sample proportion is inflated—a form of selection bias upward."),
    (40, "C", r"Two independent cross-sectional surveys describe prevalence; no exposure is manipulated, so this is descriptive."),
    (41, "A", r"$\hat{p}_2 - \hat{p}_1 = 110/990 - 180/970 \approx -0.074$."),
    (42, "D", r"$\text{SE} = \sqrt{\hat{p}_1(1-\hat{p}_1)/970 + \hat{p}_2(1-\hat{p}_2)/990}$."),
    (43, "D", r"A 99\% two-sided CI uses $z_{0.995}$: $(\hat{p}_2 - \hat{p}_1) \pm z_{0.995}\,\text{SE}$."),
    (44, "A", r"The entire 99\% CI is negative, supporting a reduction in the proportion of daily smokers between 2010 and 2020."),
    (45, "C", r"Participants were randomised to intervention or control, so this is an experimental analytic randomised controlled trial."),
    (46, "C", r"To compare population means: $H_0\!:\mu_I = \mu_C$ versus $H_A\!:\mu_I \ne \mu_C$."),
    (47, "B", r"$\text{SE} = \sqrt{24/102 + 12.5/91} \approx 0.61$ units of reduction."),
    (48, "A", r"Test statistic $t = (9.6 - 8.3)/0.61 \approx 2.13$."),
    (49, "D", r"For a two-sided $t$-test use $2\,(1 - \operatorname{pt}(|t|,\nu))$."),
    (50, "C", r"With $p=0.0345 < 0.05$ we reject $H_0$ and conclude there is evidence of a difference in mean mercury reduction between groups."),
    (51, "D", r"The $p$-value is the probability, under $H_0$, of observing a difference at least as extreme as 1.3 units (in absolute value)."),
    (52, "C", r"Increasing both the sample sizes and the significance level (e.g. $\alpha=0.1$) increases statistical power."),
    (53, "B", r"Farmer odds $= 53/447 \approx 0.119$."),
    (54, "D", r"Non-farmer odds $= 27/473 \approx 0.057$."),
    (55, "A", r"Odds ratio $= (53/447)/(27/473) = (53\times 473)/(447\times 27) \approx 2.08$."),
    (56, "E", r"$\text{SE}_{\log \text{OR}} = \sqrt{1/53 + 1/27 + 1/447 + 1/473} \approx 0.2455$."),
    (57, "B", r"Exponentiating $(0.2499, 1.2121)$ yields $(e^{0.2499}, e^{1.2121}) \approx (1.28, 3.36)$."),
    (58, "A", r"For an odds ratio, bounds entirely above/below 1 indicate increased/decreased odds; intervals spanning 1 imply insufficient evidence."),
    (59, "A", r"Missed diagnoses among farmers reduce observed cases, biasing the OR downward; this is information bias."),
    (60, "C", r"If farmers are more often male and males have lower MDD risk, sex confounding would pull the crude odds ratio toward 1, masking part of the association."),
    (61, "D", r"The adjusted OR of 1.37 has a 95\% CI that includes 1, so after adjustment the data do not show a statistically significant association."),
    (62, "E", r"$H_0$: diagnosis and paternal age are independent; $H_A$: there is an association."),
    (63, "A", r"Expected count $= (20\times 528)/1612 \approx 6.55$ children."),
    (64, "B", r"Degrees of freedom $(r-1)(c-1) = (2-1)(3-1) = 2$."),
    (65, "C", r"Right-tail $p$-value is $1 - \operatorname{pchisq}(13.30,\nu)$."),
    (66, "A", r"With $p=0.0014 < 0.05$ we reject $H_0$ and infer an association between paternal age and autism diagnosis."),
    (67, "C", r"Retinol level is modelled as the response variable and age as the explanatory variable."),
    (68, "A", r"The fitted slope is about $3.07$ ng/mL per year, as shown in the regression output."),
    (69, "C", r"Test $H_0\!:\beta_1 = 0$ versus $H_A\!:\beta_1 \ne 0$ for the age slope."),
    (70, "C", r"For simple regression with $n=100$, the $t$-statistic uses $\nu = n-2 = 98$ degrees of freedom."),
    (71, "E", r"The $p$-value $0.0172 < 0.05$ provides evidence of an association between age and retinol levels."),
    (72, "E", r"The intercept estimates the mean retinol level when age $=0$, i.e., for a newborn."),
    (73, "B", r"$\hat{\beta}_1$ estimates the mean change in retinol level for each additional year of age."),
    (74, "C", r"$R^2 = 0.05654$ indicates that about $5.654\%$ of the variance in retinol levels is explained by age."),
    (75, "D", r"Predicted value: $441.86 + 3.07\times 50 \approx 595.36$ ng/mL."),
    (76, "B", r"A 95\% prediction interval gives the range where a new 40-year-old's retinol level would fall with probability 0.95."),
    (77, "D", r"Prediction errors grow as age moves away from the sample mean (50.61 years), so forecasts at 40.61 years are less precise."),
    (78, "B", r"Predicted for age $=42$: $441.86 + 3.07\times 42 = 570.8$; residual $= 580.7 - 570.8 \approx 9.9$ ng/mL."),
    (79, "A", r"To model a binary outcome (cancer) with a continuous predictor, use logistic regression with cancer as the response."),
    (80, "E", r"The model predicts medical costs (charges), so charges is the response variable."),
    (81, "B", r"$\hat{y} = -12052.46 + 257.73\times 50 -128.64\times 1 + 322.36\times 28 + 474.41\times 3 + 23823.39\times 0 \approx 1.12\times 10^4$ dollars."),
    (82, "B", r"$\hat{\beta}_{\text{bmi}}$ estimates the change in expected charges for each one-unit BMI increase while holding the other predictors fixed."),
    (83, "A", r"The CI for the age slope is $257.73 \pm t_{0.975,1332}\times 11.9$."),
    (84, "C", r"The five predictors jointly explain about $74.97\%$ of the variation in medical charges."),
    (85, "C", r"$\mu_i$ denotes the population mean reduction for pesticide $i$, and $e_{ij}$ is the residual for plot $j$ using pesticide $i$."),
    (86, "A", r"ANOVA assumes $e_{ij}$ are independent $N(0,\sigma^2)$ within each group (common variance and zero mean)."),
    (87, "C", r"$H_0$: $\mu_A=\mu_B=\mu_C=\mu_D=\mu_E=\mu_F$ versus the alternative that not all population means are equal."),
    (88, "B", r"From the ANOVA table, total SS $=2668.8+1015.2=3684.0$ and residual SS $=1015.2$."),
    (89, "D", r"Large between-group variability relative to within-group noise favours rejecting $H_0$ in one-way ANOVA."),
    (90, "C", r"The F-test $p$-value is $\operatorname{pf}(f,5,66,\text{lower.tail}=\text{FALSE})$."),
    (91, "C", r"The p-value $<0.01$ leads to rejecting $H_0$, indicating different mean reductions among at least some pesticides."),
    (92, "B", r"Blocking on country would absorb part of the residual variation, improving sensitivity to detect pesticide effects."),
]

HEADER = r"""\documentclass[11pt]{article}
\usepackage{geometry}
\geometry{margin=1in}
\usepackage{amsmath}
\usepackage{enumitem}
\usepackage{booktabs}

\title{STAT115 2024 Practice Exam Solutions}
\author{Compiled via Codex}
\date{}

\begin{document}
\maketitle

\begin{enumerate}[label=\textbf{Q\arabic*:}, leftmargin=*, itemsep=0.9em]
"""

FOOTER = r"""\end{enumerate}
\end{document}
"""


def build_items():
    lines = []
    for number, answer, explanation in SOLUTIONS:
        lines.append(
            rf"\item \textbf{{Answer: {answer}.}} {explanation}"
        )
    return "\n".join(lines)


def main() -> None:
    if len(SOLUTIONS) != 92:
        raise ValueError(f"Expected 92 solutions, found {len(SOLUTIONS)}")
    content = HEADER + build_items() + "\n" + FOOTER
    output_path = Path('practice_exams/practice-exam-stats115-2024-solutions.tex')
    output_path.write_text(content)
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
