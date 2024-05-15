import { Order } from '../models/Order';

export interface OrderService {
  createOrder(total: number, status: 'Created' | 'Paid' | 'Sent'): Promise<Order>;
  ordersList(): Promise<Order[]>;
  updateOrder(orderId: string, status: 'Created' | 'Paid' | 'Sent'): Promise<Order | null>;
}
