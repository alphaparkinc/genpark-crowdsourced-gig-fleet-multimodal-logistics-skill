class CrowdsourcedGigFleetMultimodalLogisticsClient:
    def match_gig_rider_for_hyperlocal(self, pickup_lat=12.9716, pickup_lon=77.5946, package_weight_kg=3.5):
        return {
            'task_assignment_id': 'shd_tsk_7721',
            'assigned_gig_rider_id': 'RIDER_BLR_5521',
            'transport_mode': 'ELECTRIC_TWO_WHEELER',
            'rider_arrival_at_pickup_mins': 4.2,
            'reverse_pickup_rto_verified': True,
            'multimodal_intercity_handoff_hub': 'BANGALORE_CENTRAL_SORT_FACILITY',
            'sla_on_time_delivery_guarantee_pct': 99.4
        }
