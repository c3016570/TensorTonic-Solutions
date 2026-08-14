from typing import List, Dict


class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """

    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0

        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"

    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """

        # Extract unique words
        tokens = sorted(
            set(" ".join(texts).lower().split())
        )

        # Add special tokens
        vocab = [
            self.pad_token,
            self.unk_token,
            self.bos_token,
            self.eos_token
        ] + tokens

        # Word -> ID
        self.word_to_id = {
            word: i
            for i, word in enumerate(vocab)
        }

        # ID -> Word
        self.id_to_word = {
            i: word
            for word, i in self.word_to_id.items()
        }

        self.vocab_size = len(vocab)

    def encode(self, text: str) -> List[int]:
        """
        Convert text to a list of token IDs.
        Unknown words are mapped to <UNK>.
        """

        words = text.lower().split()

        return [
            self.word_to_id.get(
                word,
                self.word_to_id[self.unk_token]
            )
            for word in words
        ]

    def decode(self, ids: List[int]) -> str:
        """
        Convert a list of token IDs back to text.
        Unknown IDs are mapped to <UNK>.
        """

        words = [
            self.id_to_word.get(
                token_id,
                self.unk_token
            )
            for token_id in ids
        ]

        return " ".join(words)