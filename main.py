import random
import string

# Generates a secure password with a mix of uppercase, lowercase, and digits
def generate_password(segments=3, segment_length=6):
    # Separate character pools
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    
    # Full pool combining all types
    character_pool = lowercase_letters + uppercase_letters + digits
    
    segments_list = []
    for _ in range(segments):
        # Ensure each segment contains at least one uppercase, one lowercase, and one digit
        segment = (
            random.choice(lowercase_letters) + 
            random.choice(uppercase_letters) + 
            random.choice(digits)
        )
        # Fill the rest of the segment with random characters from the full pool
        segment += ''.join(random.choices(character_pool, k=segment_length - 3))
        # Shuffle the segment to distribute character types randomly
        segment = ''.join(random.sample(segment, len(segment)))
        segments_list.append(segment)
    
    # Combine the segments with dashes
    password = '-'.join(segments_list)
    return password

# MAIN
if __name__ == "__main__":
    # Password settings
    segments = 4
    segment_length = 8

    # Generate password
    generated_password = generate_password(segments, segment_length)
    print(f"Generated Password: {generated_password}")