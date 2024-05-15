export interface Order {
    id: string;
    total: number;
    status: 'Created' | 'Paid' | 'Sent';
    date: Date;
  }
  