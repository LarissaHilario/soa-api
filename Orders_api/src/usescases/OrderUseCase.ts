import { OrderService } from '../domain/services/OrderService';
import { Order } from '../domain/models/Order';

export class OrderUseCase {
  constructor(private orderService: OrderService) { }

  async createOrder(total: number, status: 'Created' | 'Paid' | 'Sent'): Promise<Order> {
    try {
      const order = await this.orderService.createOrder(total, status);
      return order;
    } catch (error) {
      throw new Error('Error creating order');
    }
  }


  async ordersList(): Promise<Order[]> {
    return this.orderService.ordersList();
  }

  async updateOrder(orderId: string, status: 'Created' | 'Paid' | 'Sent'): Promise<Order | null> {
    return this.orderService.updateOrder(orderId, status);
  }
}
