@startuml
entity User {
  +id: int <<PK>>
  --
  username: varchar(255) <<Unique>>
  email: varchar(255) <<Unique>>
  password: varchar(255)
  created_at: timestamp
}

entity Post {
  +id: int <<PK>>
  --
  content: text
  created_at: timestamp
  user_id: int <<FK>>
}

entity Comment {
  +id: int <<PK>>
  --
  content: text
  created_at: timestamp
  post_id: int <<FK>>
  user_id: int <<FK>>
}

entity Like {
  +id: int <<PK>>
  --
  created_at: timestamp
  post_id: int <<FK>>
  user_id: int <<FK>>
}

entity Share {
  +id: int <<PK>>
  --
  created_at: timestamp
  post_id: int <<FK>>
  user_id: int <<FK>>
}

entity Friendship {
  +id: int <<PK>>
  --
  follower_id: int <<FK>>
  followee_id: int <<FK>>
  created_at: timestamp
}

User ||--o{ Post: "creates"
User ||--o{ Comment: "makes"
User ||--o{ Like: "likes"
User ||--o{ Share: "shares"
User ||--o{ Friendship: "follows"

Post ||--o{ Comment: "has"
Post ||--o{ Like: "receives"
Post ||--o{ Share: "is shared"
@enduml
