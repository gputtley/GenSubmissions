# GenSubmissions

## Submitting each analysis step crab jobs

To submit LHEGEN crab jobs for all tarball files run a command like:

```bash
python run_gridpacks.py --run_all --year=2018
```

To run future steps, you can run the identical command. The templates/cmssw_to_use_YEAR.txt keeps track of what stage you are at.

## Checking and resubmitting crab jobs

To check and resubmit jobs you can use the check_and_resubmit_crab_jobs.py scripts. For gen jobs, as they create their own crab directory, you will need to run a command like this:

```bash
python check_and_resubmit_crab_jobs.py --multiple_directories --resubmit
```

For all later stages you can plug in the crab submission directory as input.

```bash
python check_and_resubmit_crab_jobs.py --directory=PREMIX --resubmit
```

If you want to resubmit jobs when you are idle, you can add options like --duration=300 --interval=30. This will try and resubmit jobs every 30 minutes for 5 hours.

## Getting miniaod tasks

Once you have finished running miniaod jobs you will need to get the output locations to run ntuples. To do this you can run this script:

```bash
python get_miniaod_tasks.py --year=2018
```

