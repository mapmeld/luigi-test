# luigi-test

Setup to experiment with Luigi tasks

## Setup

* Create a ```.luigi``` directory in your home directory
* Add the ```.luigi``` directory to your PYTHONPATH
* Create a Python program similar to ```counter.py```
* Put the Python program into the ```.luigi``` directory

## Running the code

Remember to modify the Python file in the ```.luigi``` directory and not just in
your local repo.

### Local Scheduler

Run on the command line:

```luigi --module counter Counter --x 123 --local-scheduler```

This could have conflicts if not managed by the central scheduler.

### Central Scheduler and Server

Start the luigid server:

```luigid --background --logdir ~/.luigi```

You should now have a server running on ```http://localhost:8082/```

Run a task on the command line without the local-scheduler flag

```luigi --module counter Counter --x 201```

The task should appear as Running and later as Done.

<img src="http://i.imgur.com/5JmHzAg.png"/>

## License

MIT license
