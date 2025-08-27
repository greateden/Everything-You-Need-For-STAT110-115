#### DATA IMPORT & EXPLORATION ####

# Import CSV
data <- read.csv("myfile.csv")            # read CSV into data.frame

# View / subset
head(data)                                # first 6 rows
summary(data)                             # basic summaries
subset1 <- subset(data, Group == "A")     # rows where Group equals "A"

#### DESCRIPTIVE STATISTICS ####

x <- data$variable
mean(x)                                   # sample mean
sd(x)                                     # sample standard deviation
var(x)                                    # sample variance (uses n–1)
median(x)                                 # median

#### PROBABILITY DISTRIBUTIONS ####

# Normal distribution (Z ~ N(0,1))
pnorm(q)                                  # Pr(Z ≤ q)
pnorm(q, mean=μ, sd=σ)                    # Pr(Y ≤ q) for Y~N(μ,σ)
qnorm(p)                                  # quantile (inverse cdf) of Z
qnorm(p, mean=μ, sd=σ)                    # quantile of Y~N(μ,σ)

# t-distribution
pt(t, df)                                 # Pr(T ≤ t) for T~t_df
qt(p, df)                                 # t-quantile for given tail p

# Binomial distribution
dbinom(x, size=n, prob=π)                 # Pr(X = x)
pbinom(q, size=n, prob=π)                 # Pr(X ≤ q)
rbinom(n, size=k, prob=π)                 # simulate n binomials

#### CONFIDENCE INTERVALS & HYPOTHESIS TESTS ####

# One-sample t-test for mean μ0
t.test(x, mu = μ0, conf.level = 0.95)     # returns CI, t, df, p-value

# Two-sample t-test
t.test(x, y, var.equal = TRUE)            # pooled‐var t-test
t.test(x, y, var.equal = FALSE)           # Welch’s t-test

#### LINEAR MODELS & REGRESSION ####

# Simple linear regression: Y ~ X
AVERYLONGNAMEEEEEEE <- lm(Y ~ X, data = data)             # fit model
summary(AVERYLONGNAMEEEEEEE)                              # coefficients, R², F, residuals
cor(x, y)                                   # correlation coefficient, r
confint(AVERYLONGNAMEEEEEEE, level = 0.95)                # CI for β0, β1

#### DATA VISUALIZATION (base R) ####

hist(x, main="Histogram", xlab="x", breaks=20)                         # histogram
plot(X, Y, main="Scatterplot", xlab="X", ylab="Y")                     # scatter
#### UTILITY ####

# help
?lm                                       # show lm documentation
example(t.test)                            # run examples for t.test

# clear workspace
rm(list = ls())                            # remove all objects

## ── Data import & exploration ────────────────────────────────────────────────
read.csv("file.csv")        # Base-R reader; needs working-dir set first! 
head(df);  tail(df)         # Quick peeks at the first / last rows
str(df)                     # Compact structure – catches mis-typed factors

## ── Simple summaries & graphics ──────────────────────────────────────────────
hist(df$var)                # Fast histogram; use xlab / main for labels  
mean(x); median(x); sd(x); var(x)   # Remember NA handling:  mean(x, na.rm = TRUE)

## ── Two-way tables & χ² tests ────────────────────────────────────────────────
tab  <- table(df$A, df$B)   # Contingency table (rows, columns)  
addmargins(tab)             # Adds row & column totals
chisq.test(tab)             # Test of independence; check expected counts!

## ── One- & two-sample tests for proportions ──────────────────────────────────
prop.test(x = c(18, 12),            # successes  
          n = c(30, 30),            # sample sizes
          correct = TRUE)           # continuity corr. (default TRUE)

## ── One-sample (or paired / two-sample) t-tests ──────────────────────────────
t.test(vec, mu = 0)          # One-sample H₀: μ = 0
t.test(y ~ group, data = df) # Two-sample; Welch by default

## ── Simple linear regression & friends ───────────────────────────────────────
mod <- lm(y ~ x, data = df)  # Fit line ŷ = β₀ + β₁x
summary(mod)                 # Coefs, SEs, F, R²
confint(mod)                 # 95 % CIs for β₀, β₁
predict(mod,
        newdata = data.frame(x = c(10, 15)),
        interval = "confidence")     # CI for mean at x₀
## ── One-way ANOVA & multiple comparisons ────────────────────────────────────
a1  <- aov(y ~ group, data = df)     # Same syntax as lm()
TukeyHSD(a1)                         # Pairwise CIs / pvals, controls FWER

## ── Distribution helpers (critical values & p-values) ────────────────────────
pnorm(z)            # Φ(z): P(Z ≤ z) for Z ~ N(0,1)
qnorm(p)            # z_p  : inverse of Φ
pchisq(q, df)       # P(Χ² ≤ q) 
pf(F, df1, df2)     # P(F_{df1,df2} ≤ F)
## ── Simulation snippets (great for intuition checks) ─────────────────────────
set.seed(123)                       # Reproducibility is king
x <- rnorm(1000, mean = 0, sd = 1)  # Normal draws for CLT demos
# Example: 10 000 sample means from N(μ,σ²)
ybar <- replicate(1e4, mean(rnorm(50, 0, 1)))