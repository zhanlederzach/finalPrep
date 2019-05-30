
export interface ITaskList {
  id: number;
  name: string;
}

export interface ITask {
  id: number;
  name: string;
  due_on: Date;
  created_at: Date;
  status: string;
}

export const deserializeITask = (t: any) => {
  const r = {
    id: t.id,
    name: t.name,
    due_on: new Date(t.due_on),
    created_at: new Date(t.created_at),
    status: t.status
  };
  return r;
};

export interface IPost {
  id: number;
  title: string;
  body: string;
  like_count: number;
}

export interface IAuthResponse {
  token: string;
}

export interface IContact {
  id: number;
  name: string;
  phone: string;
  my_or_not?: boolean;
}

export interface IQuery {
  query?: string;
  sort_by_name?: boolean;
  only_mine?: boolean;
}
