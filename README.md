# TCN-BAPred: a universal Bioactive Peptides Predictor Integrating Multiple Feature Representations

Biologically active peptides play crucial roles in various biological processes and demonstrate significant therapeutic potential. Predicting and identifying these peptide sequences is a critical step in understanding their functions and leveraging their benefits in medical applications. However, due to the diversity and complexity of bioactive peptides, peptide sequence identification remains a challenging issue. Moreover, traditional experimental identification methods are costly and time-consuming, limiting their feasibility in practical applications. In recent years, with the advancement of artificial intelligence technology, researchers have begun to utilize machine learning approaches to identify bioactive peptides. Despite significant progress, improving predictive performance remains a pressing issue. In this scientific study, we propose a novel method called TCN-BAPred for the efficient and rapid identification of bioactive peptides. TCN-BAPred leverages Temporal Convolutional Networks (TCN) to extract temporal dependencies in peptide sequences, enabling a comprehensive analysis of the dynamic characteristics of bioactive peptides. Additionally, we have developed a deep feature mining method, FVG, to capture global relationships among amino acids in the peptide sequence. By integrating advanced local sequence feature extraction methods, FVG provides a detailed characterization of peptide structure and function. In this work, TCN-BAPred outperforms state-of-the-art prediction methods on multiple datasets by fusing results from three channels, demonstrating that this collaborative integration enhances the accuracy and reliability of bioactive peptide prediction. Furthermore, the method exhibits strong generalization and robustness in predicting various types of peptide sequences, showcasing its potential in biomedical engineering applications.



# The dependencies required for TCN-BAPred to run

python 3.9.12

tensorflow 2.12.0

keras 2.12.0 

sklearn 1.2.2

numpy 1.22.0
