# Human oral bioavailability prediction

Predicts whether an orally dosed compound will achieve appreciable systemic exposure, reported at two thresholds of 20% and 50% bioavailability. HobPre, from Wei and colleagues, was trained on curated human oral bioavailability measurements, a scarce endpoint because values come from clinical pharmacokinetic studies rather than routine assays. Each prediction is accompanied by an applicability domain flag indicating whether the query falls within the chemical space the model was fitted on.

This model was incorporated on 2023-03-27.Last packaged on 2026-03-10.

## Information
### Identifiers
- **Ersilia Identifier:** `eos2lqb`
- **Slug:** `hob-pre`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `ADME`, `Solubility`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `4`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of human oral bioavailability above 20% and above 50%, with applicability domain flags.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| hob_20perc | float | high | Probability of moderate oral bioavailability (cut-off 20%) |
| applicability_20perc | float | high | The molecule falls in the applicability domain(1) or not(0) |
| hob_50perc | float | high | Probability of high oral bioavailability (cut-off 50%) |
| applicability_50perc | float | high | The molecule falls in the applicability domain(1) or not(0) |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos2lqb](https://hub.docker.com/r/ersiliaos/eos2lqb)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2lqb.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2lqb.zip)

### Resource Consumption
- **Model Size (Mb):** `3`
- **Environment Size (Mb):** `736`
- **Image Size (Mb):** `771.07`

**Computational Performance (seconds):**
- 10 inputs: `30.78`
- 100 inputs: `55.11`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/whymin/HOB](https://github.com/whymin/HOB)
- **Publication**: [https://doi.org/10.1186/s13321-021-00580-6](https://doi.org/10.1186/s13321-021-00580-6)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [HellenNamulinda](https://github.com/HellenNamulinda)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos2lqb
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos2lqb
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
