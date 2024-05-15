import * as dotenv from 'dotenv';
dotenv.config();
export const dbConfig = {
  user: process.env.DB_USER as string,
  password: process.env.DB_PASSWORD as string,
  host: process.env.DB_HOST as string,
  database: process.env.DB_DATABASE as string,
};