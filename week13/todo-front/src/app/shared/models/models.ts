export interface TaskList{
  id: number;
  name: string;
}

export interface Task{
  id: number;
  name: string;
  created_at: Date;
  due_on: Date;
  status: string;
}

export interface IAuthResponse{
  token: string;
}