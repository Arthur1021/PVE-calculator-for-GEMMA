# PVE-calculator-for-GEMMA
PVE calculator for GWAS result from GEMMA

GEMMA is a software toolkit for fast application of linear mixed models (LMMs) and related models to genome-wide association studies (GWAS) and other large-scale data sets.

https://github.com/genetics-statistics/GEMMA

The phenotypic variation explained (PVE) is not provided by the GEMMA.

Equation:


PVE(SNP) = [2*(beta^2)*MAF*(1-MAF)]/[2*(beta^2)*MAF(1-MAF)+((se(beta))^2)*2*N*MAF*(1-MAF)]

Original paper: Shim, H., Chasman, D.I., Smith, J.D., Mora, S., Ridker, P.M., Nickerson, D.A., Krauss, R.M., and Stephens, M. (2015). A multivariate genome-wide association analysis of 10 LDL subfractions, and their response to statin treatment, in 1868 Caucasians. PLoS One 10, e0120758.

