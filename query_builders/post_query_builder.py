




class PostQueryBuilder:
    def __init__(self, connection):
        self.connection = connection

    def create_post(self, user_id, content):
        with self.connection.cursor() as cur:
            cur.execute(
                'INSERT INTO "Post" (user_id, content) VALUES (%s, %s) RETURNING id',
                (user_id, content)
            )
            post_id = cur.fetchone()[0]
            self.connection.commit()
            return post_id

    def update_post(self, post_id, content):
        with self.connection.cursor() as cur:
            cur.execute(
                'UPDATE "Post" SET content = %s WHERE id = %s',
                (content, post_id)
            )
            self.connection.commit()

    def delete_post(self, post_id):
        with self.connection.cursor() as cur:
            cur.execute('DELETE FROM "Post" WHERE id = %s', (post_id,))
            self.connection.commit()

    def get_post(self, post_id):
        with self.connection.cursor() as cur:
            cur.execute(
                'SELECT id, user_id, content, created_at FROM "Post" WHERE id = %s', 
                (post_id,)
            )
            post = cur.fetchone()
            return post
