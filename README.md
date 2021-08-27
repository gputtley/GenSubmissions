# GenSubmissions

## Submitting each analysis step crab jobs

First copy all of the tarball files into this working directory.

To submit GEN-SIM crab jobs for all tarball files in your working directory run a command like:

```bash
python run_gridpacks.py --run_all --gen --year=2018
```

(This is not currently set up to do 2016, will need do to the LHE and GEN-SIM step manually)

To run future steps you can change --gen with either --premix, --aod or --miniaod. The crab submission files will automatically get the right file locations from the previous step of crab submissions folders. If you need to work in a new CMSSW to run step, copy the crab submission folders over (as well as the gridpacks - need to change this as gridpacks are large and only needed to loop over files).

To check and resubmit jobs you can use the check_and_resubmit_crab_jobs.py scripts. For gen jobs, as they create their own crab directory, you will need to run a command like this:

## Checking and resubmitting crab jobs

```bash
python check_and_resubmit_crab_jobs.py --multiple_directories --resubmit
```

For all later stages you can plug in the crab submission directory as input.

```bash
python check_and_resubmit_crab_jobs.py directory=PREMIX --resubmit
```

If you want to resubmit jobs when you are idle, you can add options like --duration=300 --interval=30. This will try and resubmit jobs every 30 minutes for 5 hours.

## Getting miniaod tasks

Once you have finished running miniaod jobs you will need to get the output locations to run ntuples. To do this you can run this script:

```bash
python get_miniaod_tasks.py --year=2018
```

