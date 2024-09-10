# gene-lists

Gene lists related to cancer immunotherapy

## Cancer-testis antigens

Last updated: September 10th, 2024

Sources:

- [CTpedia](http://www.cta.lncc.br/)
- [Human Protein Atlas](https://www.proteinatlas.org/)

Methodology:

- Intersection of genes in CTpedia which have at least one tissue antibody staining in HPA, keeping only expression in testis and placenta.

## Class I MHC antigen presentation

Last updated: July 21st, 2018

Sources:

- [Frequent HLA class I alterations in human prostate cancer: molecular mechanisms and clinical relevance](https://link.springer.com/article/10.1007/s00262-015-1774-5):
  - LMP2/7
  - peptide transporters TAP1/2
  - chaperones calreticulin, calnexin, ERP57, and tapasin
  - IFR-1 and NLRC5
- [Expression of Antigen Processing and Presenting Molecules in Brain Metastasis of Breast Cancer](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3365630/)
  - "β2-microgloblin, transporter associated with antigen processing (TAP) 1, TAP2 and calnexin are down-regulated in brain lesions compared with unpaired breast lesions"
- [NLRC5/MHC class I transactivator is a target for immune evasion in cancer](http://www.pnas.org/content/early/2016/05/05/1602069113.short)
- [TAPBPR: a new player in the MHC class I presentation pathway](https://www.ncbi.nlm.nih.gov/pubmed/25720504)

## Interferon-gamma response

Last updated: July 21st, 2018

Sources:

- [Interferon Receptor Signaling Pathways Regulating PD-L1 and PD-L2 Expression](https://www.sciencedirect.com/science/article/pii/S2211124717305259)
  - "JAK1/JAK2-STAT1/STAT2/STAT3-IRF1 axis primarily regulates PD-L1 expression, with IRF1 binding to its promoter"
  - "PD-L2 responded equally to interferon beta and gamma and is regulated through both IRF1 and STAT3, which bind to the PD-L2 promoter"
  - "the suppressor of cytokine signaling protein family (SOCS; mostly SOCS1 and SOCS3) are involved in negative feedback regulation of cytokines that signal mainly through JAK2 binding, thereby modulating the activity of both STAT1 and STAT3"
- [Mutations Associated with Acquired Resistance to PD-1 Blockade in Melanoma](https://www.nejm.org/doi/full/10.1056/NEJMoa1604958)
  - "resistance-associated loss-of-function mutations in the genes encoding interferon-receptor–associated Janus kinase 1 (JAK1) or Janus kinase 2 (JAK2), concurrent with deletion of the wild-type allele"
- [SOCS, inflammation, and cancer](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3772102/)
  - "Abnormal expression of SOCS1 and SOCS3 in cancer cells has been reported in human carcinoma associated with dysregulation of signals from cytokine receptors"

## Recurrently mutated cancer genes

Last updated: July 21st, 2018

Cancer genes and recurrent mutations extract from [Comprehensive Characterization of Cancer Driver Genes and Mutations](<https://www.cell.com/cell/fulltext/S0092-8674(18)30237-X>).

Genes extracted from Table S1 into `cancer-driver-genes.csv`. Mutations extracted from Table S4 into `cancer-driver-variants.csv`.

Both datasets were annotated with Ensembl IDs using Ensembl release 92.
