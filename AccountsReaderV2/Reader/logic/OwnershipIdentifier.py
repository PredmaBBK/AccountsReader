# This file extracts sentences relating to ownership and then extracts that information to a standard format (owner, subsidiary, %).
# This will consist of three lightweight neural networks:
# - Firstly, one to identify sentences relating to ownership.
# - Secondly, to find the company that is owned.
# - Finally, to find the company that owns the other.

# Depending on the size of the model, this may be run on the cloud, or the first model may be separated and run on the cloud.