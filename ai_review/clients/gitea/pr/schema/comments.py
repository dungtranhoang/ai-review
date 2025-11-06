from pydantic import BaseModel, RootModel

from ai_review.clients.gitea.pr.schema.user import GiteaUserSchema


class GiteaPRCommentSchema(BaseModel):
    id: int
    body: str
    path: str | None = None
    line: int | None = None
    user: GiteaUserSchema | None = None
    resolver: GiteaUserSchema | None = None
    position: int | None = None
    commit_id: str | None = None
    original_position: int | None = None
    original_commit_id: str | None = None
    pull_request_review_id: int | None = None


# Add schemas for review comments
class GiteaCreateReviewCommentRequestSchema(BaseModel):
    body: str
    path: str
    position: int | None = None
    line: int | None = None
    side: str = "RIGHT"  # "LEFT" or "RIGHT" 
    commit_sha: str | None = None


class GiteaCreateReviewCommentResponseSchema(BaseModel):
    id: int
    body: str
    path: str
    line: int | None = None
    position: int | None = None


class GiteaGetReviewCommentsQuerySchema(BaseModel):
    page: int = 1
    per_page: int = 100


class GiteaGetReviewCommentsResponseSchema(RootModel[list[GiteaPRCommentSchema]]):
    root: list[GiteaPRCommentSchema]


class GiteaGetPRCommentsQuerySchema(BaseModel):
    page: int = 1
    per_page: int = 100


class GiteaGetPRCommentsResponseSchema(RootModel[list[GiteaPRCommentSchema]]):
    root: list[GiteaPRCommentSchema]


class GiteaCreateCommentRequestSchema(BaseModel):
    body: str


class GiteaCreateCommentResponseSchema(BaseModel):
    id: int
    body: str
