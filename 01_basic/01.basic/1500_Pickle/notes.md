# Pickle Notes

> [Tutorial](https://www.datacamp.com/community/tutorials/pickle-python-tutorial)

## When Not To Use pickle

- If you want to use data across different programming languages, pickle is not recommended.
- Unpickling a file that was pickled in a different version of Python may not always work properly.
- You should also try not to unpickle data from an untrusted source. Malicious code inside the file might be executed upon unpickling.

