# Human oral bioavailability prediction

Prediction of human oral bioavailability for small molecules. Given SMILES, the HobPre predicts the Human oral bioavailability (HOB) value (two cutoffs of 20% and 50% for classification of molecules). The prediction is either high or low HOB.

## Identifiers

* EOS model ID: `eos2lqb`
* Slug: `human-oral-bioavailability`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Text`
* Output Type: `String`
* Output Shape: `List`
* Interpretation: This model takes smiles as input and outputs the human-oral-bioavailability(HOB) classes for both the 20% cutoff and that of 50% cutoff

## References

* [Publication](https://doi.org/10.1186/s13321-021-00580-6)
* [Source Code](https://github.com/whymin/HOB)
* Ersilia contributor: [HellenNamulinda](https://github.com/HellenNamulinda)

## Citation

If you use this model, please cite the [original authors](https://doi.org/10.1186/s13321-021-00580-6) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a CC license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!