# Phenotypic variation explained (PVE) for Genome-wide Efficient Mixed Model Association (GEMMA)
## PVE calculator for GEMMA

    GEMMA is a software toolkit for fast application of linear mixed models (LMMs) and related models to genome-wide 
    association studies (GWAS) and other large-scale data sets.

    https://github.com/genetics-statistics/GEMMA

    The phenotypic variation explained (PVE) by each SNP is not provided by the GEMMA.


## Run PVE calculator

    python PVE_calculator.py -h
        
    usage: PVE_calculator.py [-h] -i I -n N -o O
    This script is used to calculate PVE from GEMMA association result.
        
    options:
        -h, --help  show this help message and exit
        -i I  input file, association result from GEMMA, required
        -n N  number of sample size, required
        -o O  output file, association result with PVE, required


## Example:

    python PVE_calculator.py -i result.assoc.txt -n 393 -o result_pve.assoc.txt

    input file format:
    
    chr     rs      ps      n_miss  allele1 allele0 af      beta    se      logl_H1 l_remle p_wald
    1       SNP1     4299    3       A       G       0.146   5.719998e-03    7.461198e-02    -3.474714e+02   1.000000e+05
    1       SNP2     9233    1       C       T       0.149   -5.827880e-03   7.279702e-02    -3.474784e+02   1.000000e+05

## Method 

    from S1_Text.pdf
    Shim, H., Chasman, D. I., Smith, J. D., Mora, S., Ridker, P. M., Nickerson, D. A., ... & Stephens, M. (2015). 
    A multivariate genome-wide association analysis of 10 LDL subfractions, and their response to statin treatment, 
    in 1868 Caucasians. PLoS one, 10(4), e0120758.


