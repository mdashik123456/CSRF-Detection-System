class TokenValidator:
    def is_token_valid(self, token):
        """Check if the token has a minimum of 32 characters."""
        return len(token) >= 32

    def are_all_tokens_valid(self, tokens):
        """Check if all tokens in all forms are valid."""
        for form, token_list in tokens.items():
            for token in token_list:
                if not self.is_token_valid(token):
                    return False, form
        return True, None

    def are_tokens_unique(self, tokens, new_tokens):
        """Check if all tokens across forms are unique."""
        # all_tokens = [token for token_list in tokens.values() for token in token_list]
        # return len(all_tokens) == len(set(all_tokens))
        return tokens == new_tokens