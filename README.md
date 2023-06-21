# Human oral bioavailability prediction

HobPre predicts the oral bioavailability of small molecules in humans. It has been trained using public data on ~1200 molecules (Falcón-Cano et al, 2020, complemented with other literature and ChEMBL compounds). The molecules were labeled according to two cut-offs: HOB > 20% and HOB > 50%, due to ongoing discussions as to which would be a more appropriate cut-off.

## Identifiers

* EOS model ID: `eos2lqb`
* Slug: `hob-pre`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Probability of a compound having high oral bioavailability (HOB >20% and HOB >50%)

## References

* [Publication](https://doi.org/10.1186/s13321-021-00580-6)
* [Source Code](https://github.com/whymin/HOB)
* Ersilia contributor: [HellenNamulinda](https://github.com/HellenNamulinda)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos2lqb)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2lqb.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos2lqb) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://doi.org/10.1186/s13321-021-00580-6) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!