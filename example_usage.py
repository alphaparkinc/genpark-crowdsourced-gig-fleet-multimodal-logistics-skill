from client import CrowdsourcedGigFleetMultimodalLogisticsClient

def main():
    client = CrowdsourcedGigFleetMultimodalLogisticsClient()
    res = client.match_gig_rider_for_hyperlocal(28.6139, 77.2090, 5.0)
    print('Task: ' + res['task_assignment_id'] + ' | Rider: ' + res['assigned_gig_rider_id'] + ' (' + res['transport_mode'] + ')')
    print('Pickup ETA: ' + str(res['rider_arrival_at_pickup_mins']) + ' mins | On-time SLA: ' + str(res['sla_on_time_delivery_guarantee_pct']) + '%')
    print('Sort Hub: ' + res['multimodal_intercity_handoff_hub'])

if __name__ == '__main__':
    main()
