# Example matching algorithm code
class User:
    def __init__(self, name, interests):
        self.name = name
        self.interests = set(interests)  # Using set for easy comparison

    def __repr__(self):
        return f"{self.name} ({', '.join(self.interests)})"


class FriendGroupMatcher:
    def __init__(self, users):
        self.users = users

    def find_matches(self, min_common_interests=2):
        matches = []
        for i in range(len(self.users)):
            for j in range(i + 1, len(self.users)):
                common_interests = self.users[i].interests & self.users[j].interests
                if len(common_interests) >= min_common_interests:
                    matches.append((self.users[i], self.users[j], common_interests))
        return matches


# Example user data
users = [
    User("Alice", ["sports", "music", "travel"]),
    User("Bob", ["sports", "reading", "coding"]),
    User("Charlie", ["sports", "music", "movies"]),
    User("David", ["cooking", "coding", "travel"]),
    User("Eve", ["music", "reading", "sports"])
]

# Create the matching engine
matcher = FriendGroupMatcher(users)

# Find matches with at least 2 common interests
matches = matcher.find_matches(min_common_interests=2)

# Print the results
if matches:
    print("Friend Group Matches:")
    for user1, user2, common_interests in matches:
        print(f"{user1.name} and {user2.name} have {len(common_interests)} common interests: {', '.join(common_interests)}")
else:
    print("No matches found.")
