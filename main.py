import asyncio

from precacher.precacher import stream_all_blocks_and_transactions

if __name__ == "__main__":
    asyncio.run(stream_all_blocks_and_transactions())
