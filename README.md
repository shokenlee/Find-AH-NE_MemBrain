# Find MemBrain-predicted AHs in nuclear envelope proteins

This is one of the series of the Python scirpts that was used in Figure 1A and S1A of [Lee et al. bioRxiv 2024](https://www.biorxiv.org/content/10.1101/2024.11.14.623600v2).
Describes the process of MemBrain dataset analysis and its merge with nuclear envelope proteome dataset.

Step 1: List human proteins with AH prediction by MemBrain
- `MemBrain_Find_Hs_protein.ipynb`
 - `SourceData/MemBrain` contains the original dataset from [MemBrain](http://www.csbio.sjtu.edu.cn/bioinf/MemBrain/Download.htm)
 - `IntermediateProducts` directory contains the products from the substeps

Step 2: Find nuclear envelope proteins in the proteins from step 1
- `Merge_MemBrain_NEproteins.ipynb`
 - `FinalOutput` contains the outputs from this process