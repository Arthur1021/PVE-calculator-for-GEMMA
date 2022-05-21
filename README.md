# PVE-calculator-for-GEMMA
    PVE calculator for GWAS result from GEMMA

    GEMMA is a software toolkit for fast application of linear mixed models (LMMs) and related models to genome-wide 
    association studies (GWAS) and other large-scale data sets.

    https://github.com/genetics-statistics/GEMMA

    The phenotypic variation explained (PVE) is not provided by the GEMMA.


# Run PVE calculator

    python PVE_calculator.py -h
        
    usage: PVE_calculator.py [-h] -i I -n N -o O
    This script is used to calculate PVE from GEMMA association result.
        
    options:
        -h, --help  show this help message and exit
        -i I  input file, association result from GEMMA, required
        -n N  number of sample size, required
        -o O  output file, association result with PVE, required


# Example:

    python PVE_calculator.py -i result.assoc.txt -n 393 -o result_pve.assoc.txt


# Method 

    from S1_Text.pdf
    Shim, H., Chasman, D. I., Smith, J. D., Mora, S., Ridker, P. M., Nickerson, D. A., ... & Stephens, M. (2015). 
    A multivariate genome-wide association analysis of 10 LDL subfractions, and their response to statin treatment, 
    in 1868 Caucasians. PLoS one, 10(4), e0120758.


