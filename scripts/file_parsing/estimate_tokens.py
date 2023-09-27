def estimate_tokens(prompt_body: str):
    return len(prompt_body.split(' '))


def warn_excession(num_tokens):

    if num_tokens >= 32000:    
        print(f'The number of tokens of your prompt has will exceed the maximum window length.',
              'You might want to consider breaking your query up into smaller parts, or parsing smaller folders')
        return